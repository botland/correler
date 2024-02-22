#import data
#import hdi
#import index2023_heritage
import numpy as np
from scipy.stats import pearsonr
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

def build_hdi_categories(common_countries, hdi):
  hdi_categories = [
    ("all countries", common_countries),
    ("developed countries", set(hdi.selected_countries) & common_countries),
    ("very high human development countries", set(hdi.very_high_human_development) & common_countries),
    ("high human development countries", set(hdi.high_human_development) & common_countries),
    ("medium human development countries", set(hdi.medium_human_development) & common_countries),
    ("low human development countries", set(hdi.low_human_development) & common_countries)
  ]
  return hdi_categories

def extract_latest_from_timeseries(data):
    latest = {}
    for (country, year), hours in data.items():
        if country not in latest or year > latest[country][0]:
            latest[country] = (year, hours)
    result_dict = { country: hours for country, (year, hours) in latest.items() }
    return result_dict

def log_data(data):
  values = list(data.values())
  log_values = np.log(values)
  transformed_dict = { key: log_value for key, log_value in zip(data.keys(), log_values) }
  return transformed_dict

def normalize_data_minmax(data):
  values = np.array(list(data.values()))
  normalized_values = (values - np.min(values)) / (np.max(values) - np.min(values))
  normalized_dict = {}
  for i, country in enumerate(data.keys()):
    normalized_dict[country] = normalized_values[i]
  return normalized_dict

def normalize_data_zscore(data):
    values = np.array(list(data.values()))
    mean_value = np.mean(values)
    std_dev = np.std(values)
    z_score_values = (values - mean_value) / std_dev
    normalized_dict = {}
    for i, country in enumerate(data.keys()):
        normalized_dict[country] = z_score_values[i]
    return normalized_dict

def plot_chronological_chart(data, label):
  plt.figure()
  for (country, year), value in data.items():
    plt.plot(year, value, marker='o', label=f"{label} - {country}")

  plt.xlabel("Year")
  plt.ylabel("Values")
  plt.legend()
  plt.title(label)
  plt.show()
  plt.savefig("{}.png".format(label))

def replace_zero_by_epsilon(data):
    epsilon = 1e-9
    for country, value in data.items():
        if value == 0:
            data[country] = epsilon
    return data

class DataGroup2:
  def __init__(self, group, countries, label1, label2, data1, data2=None):
    self.group = group
    self.countries = countries
    self.label1 = label1
    self.label2 = label2
    self.label2_composite = label2
    self.data1 = []
    self.data2 = []
    self.correlation_coefficient = 0
    self.pvalue = 0
    self.group_data1 = [data1[country] for country in self.countries]
    if data2 is not None:
      self.group_data2 = [data2[country] for country in self.countries]

  def calculate_correlation(self):
    if len(self.group_data1) < 2 or len(self.group_data2) < 2:
      template = "  Insufficient data for correlation: {} countries in {} and {} countries in {}"
#      print(template.format(len(self.group_data1), self.label1, len(self.group_data2), self.label2))
      return
    self.correlation_coefficient, self.pvalue = pearsonr(self.group_data1, self.group_data2)

  def calculate_ratio(self):
    # Calculate the ratio between data1 and data2 for each country in the country_list
    ratio_data = {}
    for country in self.countries:
      if country in self.data1 and country in data2:
        ratio_data[country] = self.group_data1[country] / self.group_data2[country]

    # Combine data for sorting in descending order by happiness score
    combined_data = sorted(ratio_data.items(), key=lambda x: self.group_data1[x[0]], reverse=True)

    # Truncate labels if they are longer than max_label_length
    label1_truncated = self.label1[:15]
    label2_truncated = self.label2[:15]
  
    # Print sorted country data
    print("{:<20} {:<15} {:<15} {}/{}".format("Country", label1_truncated, label2_truncated, self.label1, self.label2_composite))
    template = "{:<20} {:<15.2f} {:<15.2f} {:<.3f}"
    for country, ratio in combined_data:
      print(template.format(country, self.group_data1[country], self.group_data2[country], ratio))

  def calculate_regression_analysis(self):
    # Convert lists to NumPy arrays
    convert_data1 = np.array(self.group_data2)
    convert_data2 = np.array(self.group_data1)
  
    # Perform linear regression analysis
    X = convert_data1.reshape(-1, 1)
    y = convert_data2
    model = LinearRegression()
    model.fit(X, y)
    y_pred = model.predict(X)
  
    template = "  Regression Results: coefficient={:<.3f}, intercept=={:<.3f}, mse=={:<.3f}"
#    print(template.format(model.coef_[0], model.intercept_, mean_squared_error(y, y_pred)))
    self.plot_linear_regression(convert_data1, convert_data2, y_pred)

  def plot_annotation(self, plt, in_data1, in_data2):
    list_annotate = [ "Denmark", "France", "Germany", "Netherlands", "Switzerland", "United States" ]
    for i, country in enumerate(self.countries):
      if country in list_annotate:
        plt.annotate(country, (in_data1[i], in_data2[i]), textcoords="offset points", xytext=(5, -2), ha='left')

  def plot_info(self, plt):
    plt.title("{} vs {}\n{}".format(self.label1, self.label2_composite, self.group))
    plt.legend()
    text = "R={:<.5f}\nP={:<.5f}".format(self.correlation_coefficient, self.pvalue)
    plt.text(1.001, 0.05, text, fontsize=8, transform=plt.gca().transAxes)
#    plt.figtext(1.01, 0.05, text, fontsize=8)
    plt.show()
    plt.savefig("charts/{}_vs_{}_{}.png".format(self.label1, self.label2_composite, self.group))
    plt.close()

  def plot_linear_regression(self, in_data1, in_data2, y_pred):
    # Create XY chart with linear regression line and country names
    plt.figure()
    plt.scatter(in_data1, in_data2, label="Countries")
    plt.plot(in_data1, y_pred, color='red', label="Regression Line")
    plt.xlabel(self.label2_composite)
    plt.ylabel(self.label1)
    self.plot_annotation(plt, in_data1, in_data2);
    self.plot_info(plt)

  def show(self, correlation_threshold, pvalue_threshold, show_no=False):
    num_countries = len(self.countries)
    if num_countries > 0:
      template = "{} vs {} - {}: R={:.5f} P={:.5f} N={}"
      if show_no or (abs(self.correlation_coefficient) > correlation_threshold and float(self.pvalue) < pvalue_threshold):
        print(template.format(self.label1, self.label2_composite, self.group, self.correlation_coefficient, self.pvalue, num_countries))
#        self.calculate_ratio()
        self.calculate_regression_analysis()

class DataGroupMul(DataGroup2):
  def __init__(self, group, countries, label1, label2, label3, data1, data2, data3):
    super().__init__(group, countries, label1, label2, data1)
    self.label2_composite = "{} * {}".format(label2, label3)
    self.label3 = label3
    self.group_data2 = [data2[country] * data3[country] for country in self.countries]

  def calculate_ratio(self):
    # Calculate the ratio between data1 and data2 * data3 for each country in the country_list
    ratio_data = {}
    for country in self.countries:
      if country in self.data1 and country in self.data2 and country in self.data3:
        ratio_data[country] = self.data1[country] / (self.data2[country] * self.data3[country])

    # Combine data for sorting in descending order by happiness score
    combined_data = sorted(ratio_data.items(), key=lambda x: self.data1[x[0]], reverse=True)

    # Truncate labels if they are longer than max_label_length
    label1_truncated = self.label1[:15]
    label2_truncated = self.label2[:15]
    label3_truncated = self.label3[:15]

    # Print sorted country data
    template = "{:<20} {:<15} {:<15}*{:<15} {}/({})"
    print(template.format("Country", label1_truncated, label2_truncated, label3_truncated, self.label1, self.label2_composite))
    template = "{:<20} {:<15.2f} {:<15.2f}*{:<15.2f} {:<.3f}"
    for country, ratio in combined_data:
      print(template.format(country, self.data1[country], self.data2[country], self.data3[country], ratio))

class DataGroupDiv(DataGroup2):
  def __init__(self, group, countries, label1, label2, label3, data1, data2, data3):
    super().__init__(group, countries, label1, label2, data1)
    self.label2_composite = "{} \u2044 {}".format(label2, label3)
    self.label3 = label3
    self.group_data2 = [data2[country] / data3[country] for country in self.countries]

  def calculate_ratio(self):
    # Calculate the ratio between data1 and data2 / data3 for each country in the country_list
    ratio_data = {}
    for country in self.countries:
      if country in self.data1 and country in self.data2 and country in self.data3:
        ratio_data[country] = self.data1[country] / (self.data2[country] / self.data3[country])

    # Combine data for sorting in descending order by happiness score
    combined_data = sorted(ratio_data.items(), key=lambda x: self.data1[x[0]], reverse=True)

    # Truncate labels if they are longer than max_label_length
    label1_truncated = self.label1[:15]
    label2_truncated = self.label2[:15]
    label3_truncated = self.label3[:15]

    # Print sorted country data
    template = "{:<20} {:<15} {:<15}/{:<15} {}/({})"
    print(template.format("Country", label1_truncated, label2_truncated, label3_truncated, self.label1, self.label2_composite))
    template = "{:<20} {:<15.2f} {:<15.2f}/{:<15.2f} {:<.3f}"
    for country, ratio in combined_data:
      print(template.format(country, self.data1[country], self.data2[country], self.data3[country], ratio))

class DataGroupMulDiv(DataGroup2):
  def __init__(self, group, countries, label1, label2, label3, label4, data1, data2, data3, data4):
    super().__init__(group, countries, label1, label2, data1)
    self.label2_composite = "{} * {} \u2044 {}".format(label2, label3, label4)
    self.label3 = label3
    self.label4 = label4
    self.group_data2 = [data2[country] * data3[country] / data4[country] for country in self.countries]

  def calculate_ratio(self):
    # Calculate the ratio between data1 and data2 * data3 / data4 for each country in the country_list
    ratio_data = {}
    for country in self.countries:
      if country in self.data1 and country in self.data2 and country in self.data3 and country in self.data4:
        ratio_data[country] = self.data1[country] / (self.data2[country] * self.data3[country] / self.data4[country])

    # Combine data for sorting in descending order by happiness score
    combined_data = sorted(ratio_data.items(), key=lambda x: self.data1[x[0]], reverse=True)

    # Truncate labels if they are longer than max_label_length
    label1_truncated = self.label1[:15]
    label2_truncated = self.label2[:15]
    label3_truncated = self.label3[:15]
    label4_truncated = self.label4[:15]

    # Print sorted country data
    template = "{:<20} {:<15} {:<15}*{:<15}/{:<15} {}/({})"
    print(template.format("Country", label1_truncated, label2_truncated, label3_truncated, label4_truncated, self.label1, self.label2_composite))
    template = "{:<20} {:<15.2f} {:<15.2f}*{:<15.2f}/{:<15.2f} {:<.3f}"
    for country, ratio in combined_data:
      print(template.format(country, self.data1[country], self.data2[country], self.data3[country], self.data4[country], ratio))

class TimeSeriesDataGroup(DataGroup2):
    def __init__(self, group, data, label, year_column="Year"):
        super().__init__(group, set(country_year[0] for country_year in data.keys()), label, label, {}, {})
        self.year_column = year_column
        self.extract_data(data)

    def extract_data(self, data):
        for (country, year), value in data.items():
            if country not in self.group_data1:
                self.group_data1[country] = {}
                self.group_data2[country] = {}
            self.group_data1[country][year] = value
            self.group_data2[country][year] = value

    def plot_chronological_chart(self):
        plt.figure()
        for country in self.countries:
            if country in self.group_data1:
                years = list(self.group_data1[country].keys())
                values = list(self.group_data1[country].values())
                plt.plot(years, values, label=f"{self.label} - {country}", marker='o')
        plt.xlabel("Year")
        plt.ylabel("Values")
        plt.legend()
        plt.title("{} - {}".format(self.label, self.group))
        plt.show()

def do_calculate_correlation(label1, label2, data1, data2, hdi, correlation_threshold=0.4, pvalue_threshold=0.05, show_no=False):
  common_countries = set(data1.keys()) & set(data2.keys())
  hdi_categories = build_hdi_categories(common_countries, hdi)
  for category, common_hdi_countries in hdi_categories:
    data = DataGroup2(category, common_hdi_countries, label1, label2, data1, data2)
    data.calculate_correlation()
    data.show(correlation_threshold, pvalue_threshold, show_no)

def calculate_correlation(label1, label2, data_map, hdi, correlation_threshold=0.4, pvalue_threshold=0.05, show_no=False):
  data1 = data_map[label1]
  data2 = data_map[label2]
  do_calculate_correlation(label1, label2, data1, data2, hdi, correlation_threshold, pvalue_threshold, show_no);

def calculate_correlationlog(label1, label2, data_map, hdi, correlation_threshold=0.4, pvalue_threshold=0.05, show_no=False):
  data1 = data_map[label1]
  data2 = log_data(data_map[label2])
  do_calculate_correlation(label1, "{} (log)".format(label2), data1, data2, hdi, correlation_threshold, pvalue_threshold, show_no);

def do_calculate_correlationmul(label1, label2, label3, data1, data2, data3, hdi, correlation_threshold=0.4, pvalue_threshold=0.05):
  common_countries = set(data1.keys()) & set(data2.keys()) & set(data3.keys())
  hdi_categories = build_hdi_categories(common_countries, hdi)
  for category, common_hdi_countries in hdi_categories:
    data = DataGroupMul(category, common_hdi_countries, label1, label2, label3, data1, data2, data3)
    data.calculate_correlation()
    data.show(correlation_threshold, pvalue_threshold)

def calculate_correlationmul(label1, label2, label3, data_map, hdi, correlation_threshold=0.4, pvalue_threshold=0.05):
  data1 = data_map[label1]
  data2 = data_map[label2]
  data3 = data_map[label3]
  do_calculate_correlationmul(label1, label2, label3, data1, data2, data3, hdi, correlation_threshold, pvalue_threshold);

def calculate_correlatiolognmul(label1, label2, label3, data_map, hdi, correlation_threshold=0.4, pvalue_threshold=0.05):
  data1 = data_map[label1]
  data2 = log_data(data_map[label2])
  data3 = data_map[label3]
  do_calculate_correlationmul(label1, "{} (log)".format(label2), label3, data1, data2, data3, hdi, correlation_threshold, pvalue_threshold);

def do_calculate_correlationdiv(label1, label2, label3, data1, data2, data3, hdi, correlation_threshold=0.4, pvalue_threshold=0.05):
  common_countries = set(data1.keys()) & set(data2.keys()) & set(data3.keys())
  hdi_categories = build_hdi_categories(common_countries, hdi)
  for category, common_hdi_countries in hdi_categories:
    data = DataGroupDiv(category, common_hdi_countries, label1, label2, label3, data1, data2, data3)
    data.calculate_correlation()
    data.show(correlation_threshold, pvalue_threshold)

def calculate_correlationdiv(label1, label2, label3, data_map, hdi, correlation_threshold=0.4, pvalue_threshold=0.05):
  data1 = data_map[label1]
  data2 = data_map[label2]
  data3 = replace_zero_by_epsilon(data_map[label3])
  do_calculate_correlationdiv(label1, label2, label3, data1, data2, data3, hdi, correlation_threshold, pvalue_threshold);

def calculate_correlationlogdiv(label1, label2, label3, data_map, hdi, correlation_threshold=0.4, pvalue_threshold=0.05):
  data1 = data_map[label1]
  data2 = log_data(data_map[label2])
  data3 = replace_zero_by_epsilon(data_map[label3])
  do_calculate_correlationdiv(label1, "{} (log)".format(label2), label3, data1, data2, data3, hdi, correlation_threshold, pvalue_threshold);

def calculate_correlationmuldiv(label1, label2, label3, label4, data_map, hdi, correlation_threshold=0.4, pvalue_threshold=0.05):
  data1 = data_map[label1]
  data2 = data_map[label2]
  data3 = data_map[label3]
  data4 = data_map[label4]
  common_countries = set(data1.keys()) & set(data2.keys()) & set(data3.keys()) & set(data4.keys())
  hdi_categories = build_hdi_categories(common_countries, hdi)
  for category, common_hdi_countries in hdi_categories:
    data = DataGroupMulDiv(category, common_hdi_countries, label1, label2, label3, label4, data1, data2, data3, data4)
    data.calculate_correlation()
    data.show(correlation_threshold, pvalue_threshold)
