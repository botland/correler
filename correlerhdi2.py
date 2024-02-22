#!/usr/bin/python3.9
import library as lib
import data
import hdi
import hours_worked
import index2023_heritage

class Indicators:
  def __init__(self):
    self.average_iq = "Average IQ"
    self.capitalism = "Capitalism (economic freedom)"
    self.economic_freedom = "Economic Freedom"
    self.personal_freedom = "Personal Freedom"
    self.happiness = "Happiness"
    self.hdi = "Human Development Index"
    self.gini = "Income Inequality"
    self.gdp_per_capita = "GDP per Capita"
    self.gdp_per_capita_feeling = "Subjective GDP per Capita"
    self.hours_worked = "Hours worked"
    self.fertility = "fertility"
    self.life_expectancy = "Life expectancy"
    self.pisa = "Pisa (average maths, science, reading)"
    self.public_debt = "Public Debt"
    self.public_spending = "Public Spending"
    self.publications_per_capita = "Scientific Publications per Capita"
    self.education_spending = "Public Spending on Education"
    self.education_spending_before_tertiary = "Public Spending on Education (before tertiary)"
    self.pension_spending = "Public Spending on Pension"
    self.socialism = "Socialism (social spending)"
    self.social_spending = "Social Spending"
    self.social_security_contribution = "Social Security Contributions"
    self.social_security_contribution2 = "Contribution Rates (ISSA)"
    self.corporate_profit_tax = "Corporate Profit Tax"
    self.tax_revenue = "Tax Revenue"
    self.trust_ratio = "Trust Ratio"
    self.unemployment_rate = "Unemployment Rate"

class Indicators_heritage(Indicators):
  def __init__(self):
    self.region = "Region"
    self.world_rank = "World Rank"
    self.region_rank = "Region Rank"
    self.score_2023 = "2023 Score"
    self.change_from_2022 = "Change from 2022"
    self.property_rights = "Property Rights"
    self.judical_effectiveness = "Judicial Effectiveness"
    self.gov_integrity = "Government Integrity"
    self.tax_burden = "Tax Burden"
    self.gov_spending = "Government Spending"
    self.fiscal_health = "Fiscal Health"
    self.business_freedom = "Business Freedom"
    self.labor_freedom = "Labor Freedom"
    self.monetary_freedom = "Monetary Freedom"
    self.trade_freedom = "Trade Freedom"
    self.investment_freedom = "Investment Freedom"
    self.financial_freedom = "Financial Freedom"
    self.score_2022 = "2022 Score"

def merge_hdi(hdi):
  merge = {}
  merge.update(hdi.very_high_human_development)
  merge.update(hdi.high_human_development)
  merge.update(hdi.medium_human_development)
  merge.update(hdi.low_human_development)
  return merge

def build_data_map(ind, data, hdi):
  data_map = {}
  data_map[ind.average_iq] = data.average_iq
  data_map[ind.capitalism] = data.economic_freedom
  data_map[ind.economic_freedom] = data.economic_freedom
  data_map[ind.personal_freedom] = data.personal_freedom
  data_map[ind.happiness] = data.happiness
  data_map[ind.hdi] = merge_hdi(hdi)
  data_map[ind.gini] = data.gini
  data_map[ind.gdp_per_capita] = data.gdp_per_capita
  data_map[ind.gdp_per_capita_feeling] = data.gdp_per_capita_feeling
  data_map[ind.hours_worked] = data.hours_worked
  data_map[ind.fertility] = data.fertility
  data_map[ind.life_expectancy] = data.life_expectancy
  data_map[ind.pisa] = data.pisa_maths_science_reading
  data_map[ind.public_debt] = data.public_debt
  data_map[ind.public_spending] = data.public_spending
  data_map[ind.publications_per_capita] = data.publications_per_capita
  data_map[ind.education_spending] = data.education_spending
  data_map[ind.education_spending_before_tertiary] = data.education_spending_before_tertiary
  data_map[ind.pension_spending] = data.pension_spending
  data_map[ind.socialism] = data.social_spending
  data_map[ind.social_spending] = data.social_spending
  data_map[ind.social_security_contribution] = data.social_security
  data_map[ind.social_security_contribution2] = data.social_security_from_issa
  data_map[ind.corporate_profit_tax] = data.corporate_profit_tax
  data_map[ind.tax_revenue] = data.tax_revenue
  data_map[ind.trust_ratio] = data.trust_ratio
  data_map[ind.unemployment_rate] = data.unemployment_rate
  return data_map

def build_heritage_map(ind, data):
  map = {}
  map[ind.region] = data.Region_data
  map[ind.world_rank] = data.World_Rank_data
  map[ind.region_rank] = data.Region_Rank_data
  map[ind.score_2023] = data.Score_2022_data
  map[ind.change_from_2022] = data.Change_from_2022_data
  map[ind.property_rights] = data.Property_Rights_data
  map[ind.judical_effectiveness] = data.Judical_Effectiveness_data
  map[ind.gov_integrity] = data.Govt_Integrity_data
  map[ind.tax_burden] = data.Tax_Burden_data
  map[ind.gov_spending] = data.Govt_Spending_data
  map[ind.fiscal_health] = data.Fiscal_Health_data
  map[ind.business_freedom] = data.Business_Freedom_data
  map[ind.labor_freedom] = data.Labor_Freedom_data
  map[ind.monetary_freedom] = data.Monetary_Freedom_data
  map[ind.trade_freedom] = data.Trade_Freedom_data
  map[ind.investment_freedom] = data.Investment_Freedom_data
  map[ind.financial_freedom] = data.Financial_Freedom_data
  map[ind.score_2022] = data.Score_2022_data
  return map

def calculate_correlation_group0(ind, data_map, hdi):
  lib.calculate_correlation(ind.average_iq, ind.economic_freedom, data_map, hdi, 0.4, 0.1)
#  lib.calculate_correlation(ind.average_iq, ind.publications_per_capita, data_map, hdi, 0.4, 0.1)
  lib.calculate_correlation(ind.publications_per_capita, ind.economic_freedom, data_map, hdi, 0.4, 0.1)
  lib.calculate_correlation(ind.publications_per_capita, ind.trust_ratio, data_map, hdi, 0.4, 0.1)
  lib.calculate_correlation(ind.happiness, ind.economic_freedom, data_map, hdi, 0.4, 0.1)
  lib.calculate_correlation(ind.happiness, ind.public_debt, data_map, hdi, 0.4, 0.1)
  lib.calculate_correlation(ind.happiness, ind.public_spending, data_map, hdi, 0.4, 0.1)
  lib.calculate_correlation(ind.happiness, ind.social_spending, data_map, hdi, 0.4, 0.1)
  lib.calculate_correlation(ind.happiness, ind.social_security_contribution, data_map, hdi, 0.4, 0.1)
  lib.calculate_correlationlog(ind.happiness, ind.trust_ratio, data_map, hdi, 0.4, 0.1)
  lib.calculate_correlation(ind.trust_ratio, ind.economic_freedom, data_map, hdi, 0.4, 0.1)
  lib.calculate_correlationmul(ind.gdp_per_capita, ind.social_spending, ind.public_debt, data_map, hdi, 0.4, 0.1)
  lib.calculate_correlationmul(ind.happiness, ind.economic_freedom, ind.average_iq, data_map, hdi, 0.4, 0.1)
  lib.calculate_correlationmul(ind.happiness, ind.economic_freedom, ind.trust_ratio, data_map, hdi, 0.4, 0.1)

def calculate_correlation_group_gdp(ind, data_map, hdi):
  lib.calculate_correlation(ind.gdp_per_capita, ind.public_debt, data_map, hdi, 0.4, 0.1)
  lib.calculate_correlation(ind.gdp_per_capita, ind.social_spending, data_map, hdi, 0.4, 0.1)
  lib.calculate_correlation(ind.gdp_per_capita, ind.social_security_contribution, data_map, hdi, 0.4, 0.1)
  lib.calculate_correlationlog(ind.happiness, ind.gdp_per_capita, data_map, hdi, 0.4, 0.1)
  lib.calculate_correlationlog(ind.happiness, ind.gdp_per_capita_feeling, data_map, hdi, 0.4, 0.1)
  lib.calculate_correlationdiv(ind.happiness, ind.gdp_per_capita, ind.public_debt, data_map, hdi, 0.4, 0.1)
  lib.calculate_correlationdiv(ind.happiness, ind.gdp_per_capita_feeling, ind.public_debt, data_map, hdi, 0.4, 0.1)
  lib.calculate_correlationlogdiv(ind.happiness, ind.gdp_per_capita, ind.public_debt, data_map, hdi, 0.4, 0.1)
  lib.calculate_correlationlogdiv(ind.happiness, ind.gdp_per_capita_feeling, ind.public_debt, data_map, hdi, 0.4, 0.1)
  lib.calculate_correlationlogdiv(ind.happiness, ind.gdp_per_capita, ind.social_security_contribution, data_map, hdi, 0.4, 0.1)
  lib.calculate_correlationlogdiv(ind.happiness, ind.gdp_per_capita_feeling, ind.social_security_contribution, data_map, hdi, 0.4, 0.1)

def calculate_correlation_group_gdp_inv(ind, data_map, hdi):
  lib.calculate_correlationlog(ind.happiness, ind.gdp_per_capita, data_map, hdi, 0.0, 1.0)
  lib.calculate_correlationlog(ind.life_expectancy, ind.gdp_per_capita, data_map, hdi, 0.0, 1.0)
  lib.calculate_correlationlog(ind.pisa, ind.gdp_per_capita, data_map, hdi, 0.0, 1.0)
  lib.calculate_correlationlog(ind.publications_per_capita, ind.gdp_per_capita, data_map, hdi, 0.0, 1.0)
  lib.calculate_correlationlog(ind.personal_freedom, ind.gdp_per_capita, data_map, hdi, 0.0, 1.0)
  lib.calculate_correlationlog(ind.unemployment_rate, ind.gdp_per_capita, data_map, hdi, 0.0, 1.0)

def calculate_correlation_group_gdpadjusted_inv(ind, data_map, hdi):
  lib.calculate_correlationlogdiv(ind.happiness, ind.gdp_per_capita, ind.public_spending, data_map, hdi, 0.0, 1.0)
  lib.calculate_correlationlogdiv(ind.life_expectancy, ind.gdp_per_capita, ind.public_spending, data_map, hdi, 0.0, 1.0)
  lib.calculate_correlationlogdiv(ind.pisa, ind.gdp_per_capita, ind.public_spending, data_map, hdi, 0.0, 1.0)
  lib.calculate_correlationlogdiv(ind.publications_per_capita, ind.gdp_per_capita, ind.public_spending, data_map, hdi, 0.0, 1.0)
  lib.calculate_correlationlogdiv(ind.personal_freedom, ind.gdp_per_capita, ind.public_spending, data_map, hdi, 0.0, 1.0)
  lib.calculate_correlationlogdiv(ind.unemployment_rate, ind.gdp_per_capita, ind.public_spending, data_map, hdi, 0.0, 1.0)

def calculate_correlation_group_tax(ind, data_map, hdi):
  lib.calculate_correlation(ind.tax_revenue, ind.happiness, data_map, hdi, 0.0, 1.0)
  lib.calculate_correlation(ind.tax_revenue, ind.life_expectancy, data_map, hdi, 0.0, 1.0)
  lib.calculate_correlation(ind.tax_revenue, ind.pisa, data_map, hdi, 0.0, 1.0)
  lib.calculate_correlation(ind.tax_revenue, ind.publications_per_capita, data_map, hdi, 0.0, 1.0)
  lib.calculate_correlation(ind.tax_revenue, ind.personal_freedom, data_map, hdi, 0.0, 1.0)
  lib.calculate_correlation(ind.tax_revenue, ind.unemployment_rate, data_map, hdi, 0.0, 1.0)

def calculate_correlation_group_tax_inv(ind, data_map, hdi):
  lib.calculate_correlation(ind.happiness, ind.tax_revenue, data_map, hdi, 0.0, 1.0)
  lib.calculate_correlation(ind.life_expectancy, ind.tax_revenue, data_map, hdi, 0.0, 1.0)
  lib.calculate_correlation(ind.pisa, ind.tax_revenue, data_map, hdi, 0.0, 1.0)
  lib.calculate_correlation(ind.publications_per_capita, ind.tax_revenue, data_map, hdi, 0.0, 1.0)
  lib.calculate_correlation(ind.personal_freedom, ind.tax_revenue, data_map, hdi, 0.0, 1.0)
  lib.calculate_correlation(ind.unemployment_rate, ind.tax_revenue, data_map, hdi, 0.0, 1.0)

def calculate_correlation_group_system(indicator, data_map, hdi, correlation_threshold=0.0, pvalue_threshold=1.0):
  lib.calculate_correlation(ind.capitalism, indicator, data_map, hdi, correlation_threshold, pvalue_threshold, False)
  lib.calculate_correlation(ind.socialism, indicator, data_map, hdi, correlation_threshold, pvalue_threshold, False)

def calculate_correlation_group_systemlog(indicator, data_map, hdi, correlation_threshold=0.0, pvalue_threshold=1.0):
  lib.calculate_correlationlog(ind.capitalism, indicator, data_map, hdi, correlation_threshold, pvalue_threshold, True)
  lib.calculate_correlationlog(ind.socialism, indicator, data_map, hdi, correlation_threshold, pvalue_threshold, True)

def calculate_correlation_group_spending(ind, data_map, hdi):
  lib.calculate_correlationlog(ind.public_spending, ind.gdp_per_capita, data_map, hdi, 0.0, 1.0)
  lib.calculate_correlation(ind.public_spending, ind.gdp_per_capita, data_map, hdi, 0.0, 1.0)
  lib.calculate_correlation(ind.public_spending, ind.pisa, data_map, hdi, 0.0, 1.0)
  lib.calculate_correlation(ind.public_spending, ind.publications_per_capita, data_map, hdi, 0.0, 1.0)
  lib.calculate_correlation(ind.public_spending, ind.personal_freedom, data_map, hdi, 0.0, 1.0)
  lib.calculate_correlation(ind.public_spending, ind.unemployment_rate, data_map, hdi, 0.0, 1.0)

def calculate_correlation_group_social_happiness(ind, data_map, hdi):
  lib.calculate_correlation(ind.happiness, ind.public_debt, data_map, hdi, 0.4, 0.1)
  lib.calculate_correlation(ind.happiness, ind.public_spending, data_map, hdi, 0.4, 0.1)
  lib.calculate_correlation(ind.happiness, ind.social_spending, data_map, hdi, 0.4, 0.1)
  lib.calculate_correlation(ind.happiness, ind.social_security_contribution, data_map, hdi, 0.4, 0.1)
  lib.calculate_correlation(ind.happiness, ind.social_security_contribution2, data_map, hdi, 0.4, 0.1)

def calculate_correlation_group_socialism(ind, data_map, hdi):
  calculate_correlation_group_indicator(ind.socialism, ind, data_map, hdi)

def calculate_correlation_group_life(ind, data_map, hdi):
  lib.calculate_correlationlog(ind.life_expectancy, ind.gdp_per_capita, data_map, hdi, 0.0, 1.0)
  lib.calculate_correlation(ind.life_expectancy, ind.economic_freedom, data_map, hdi, 0.0, 1.0)
  lib.calculate_correlation(ind.life_expectancy, ind.public_spending, data_map, hdi, 0.0, 1.0)
  lib.calculate_correlation(ind.life_expectancy, ind.tax_revenue, data_map, hdi, 0.0, 1.0)

def calculate_correlation_group_money(ind, data_map, hdi):
  lib.calculate_correlationlog(ind.happiness, ind.gdp_per_capita, data_map, hdi, 0.0, 1.0)
  lib.calculate_correlation(ind.happiness, ind.public_spending, data_map, hdi, 0.0, 1.0)
  lib.calculate_correlation(ind.happiness, ind.tax_revenue, data_map, hdi, 0.0, 1.0)

def calculate_correlation_group_indicator(indicator, ind, data_map, hdi, correlation_threshold=0.5, pvalue_threshold=0.05):
  lib.calculate_correlation(indicator, ind.happiness, data_map, hdi, correlation_threshold, pvalue_threshold)
  lib.calculate_correlation(indicator, ind.hdi, data_map, hdi, correlation_threshold, pvalue_threshold)
  lib.calculate_correlation(indicator, ind.gini, data_map, hdi, correlation_threshold, pvalue_threshold)
  lib.calculate_correlationlog(indicator, ind.gdp_per_capita, data_map, hdi, correlation_threshold, pvalue_threshold)
  lib.calculate_correlation(indicator, ind.hours_worked, data_map, hdi, correlation_threshold, pvalue_threshold)
  lib.calculate_correlation(indicator, ind.life_expectancy, data_map, hdi, correlation_threshold, pvalue_threshold)
  lib.calculate_correlation(indicator, ind.personal_freedom, data_map, hdi, correlation_threshold, pvalue_threshold)
  lib.calculate_correlation(indicator, ind.pisa, data_map, hdi, correlation_threshold, pvalue_threshold)
  lib.calculate_correlation(indicator, ind.public_debt, data_map, hdi, correlation_threshold, pvalue_threshold)
  lib.calculate_correlation(indicator, ind.public_spending, data_map, hdi, correlation_threshold, pvalue_threshold)
  lib.calculate_correlation(indicator, ind.education_spending, data_map, hdi, correlation_threshold, pvalue_threshold)
  lib.calculate_correlation(indicator, ind.pension_spending, data_map, hdi, correlation_threshold, pvalue_threshold)
  lib.calculate_correlation(indicator, ind.social_spending, data_map, hdi, correlation_threshold, pvalue_threshold)
  lib.calculate_correlation(indicator, ind.social_security_contribution, data_map, hdi, correlation_threshold, pvalue_threshold)
  lib.calculate_correlation(indicator, ind.corporate_profit_tax, data_map, hdi, correlation_threshold, pvalue_threshold)
  lib.calculate_correlation(indicator, ind.tax_revenue, data_map, hdi, correlation_threshold, pvalue_threshold)
  lib.calculate_correlation(indicator, ind.unemployment_rate, data_map, hdi, correlation_threshold, pvalue_threshold)

def calculate_correlation_group_indicator3(ind1, ind2, ind3, data_map, hdi, correlation_threshold=0.0, pvalue_threshold=1.0):
  lib.calculate_correlation(ind1, ind3, data_map, hdi, correlation_threshold, pvalue_threshold)
  lib.calculate_correlation(ind2, ind3, data_map, hdi, correlation_threshold, pvalue_threshold)

def calculate_correlation_group_indicator3log(ind1, ind2, ind3, data_map, hdi, correlation_threshold=0.0, pvalue_threshold=1.0):
  lib.calculate_correlationlog(ind1, ind3, data_map, hdi, correlation_threshold, pvalue_threshold)
  lib.calculate_correlationlog(ind2, ind3, data_map, hdi, correlation_threshold, pvalue_threshold)

def calculate_correlation_group_hdi(ind, data_map, hdi):
  lib.calculate_correlation(ind.hdi, ind.pisa, data_map, hdi, 0.0, 1.0)
  lib.calculate_correlation(ind.hdi, ind.publications_per_capita, data_map, hdi, 0.0, 1.0)
  lib.calculate_correlation(ind.hdi, ind.public_spending, data_map, hdi, 0.0, 1.0)
  lib.calculate_correlation(ind.hdi, ind.tax_revenue, data_map, hdi, 0.0, 1.0)

def calculate_correlation_group_happiness(ind, data_map, hdi):
  lib.calculate_correlationlog(ind.happiness, ind.gdp_per_capita, data_map, hdi, 0.0, 1.0)
  lib.calculate_correlation(ind.happiness, ind.economic_freedom, data_map, hdi, 0.0, 1.0)
  lib.calculate_correlation(ind.happiness, ind.public_spending, data_map, hdi, 0.0, 1.0)
  lib.calculate_correlation(ind.happiness, ind.tax_revenue, data_map, hdi, 0.0, 1.0)

def calculate_correlation_group_freedom(ind, data_map, hdi):
  calculate_correlation_group_indicator(ind.economic_freedom, ind, data_map, hdi)

def calculate_correlation_group_education(ind, data_map, hdi):
  calculate_correlation_group_indicator(ind.pisa, ind, data_map, hdi, 0.0, 1.0)

def calculate_correlation_group_capitalism(ind, data_map, hdi):
  calculate_correlation_group_indicator(ind.capitalism, ind, data_map, hdi)

def calculate_correlation_group1(ind, data_map, hdi):
  lib.calculate_correlation(ind.happiness, ind.economic_freedom, data_map, hdi)
  lib.calculate_correlation(ind.happiness, ind.hdi, data_map, hdi)
  lib.calculate_correlation(ind.happiness, ind.gini, data_map, hdi)
  lib.calculate_correlation(ind.happiness, ind.gdp_per_capita, data_map, hdi)
  lib.calculate_correlation(ind.happiness, ind.public_debt, data_map, hdi)
  lib.calculate_correlation(ind.happiness, ind.public_spending, data_map, hdi)
  lib.calculate_correlation(ind.happiness, ind.pension_spending, data_map, hdi)
  lib.calculate_correlation(ind.happiness, ind.social_spending, data_map, hdi)
  lib.calculate_correlation(ind.happiness, ind.social_security_contribution, data_map, hdi)
  lib.calculate_correlation(ind.happiness, ind.corporate_profit_tax, data_map, hdi)
  lib.calculate_correlation(ind.happiness, ind.tax_revenue, data_map, hdi)
  lib.calculate_correlation(ind.happiness, ind.unemployment_rate, data_map, hdi)

def calculate_correlation_group2(ind, data_map, hdi):
  lib.calculate_correlationmul(ind.happiness, ind.gini, ind.public_debt, data_map, hdi)
  lib.calculate_correlationmul(ind.happiness, ind.gini, ind.public_spending, data_map, hdi)
  lib.calculate_correlationmul(ind.happiness, ind.social_security_contribution, ind.public_spending, data_map, hdi)
  lib.calculate_correlationmul(ind.happiness, ind.social_security_contribution, ind.public_debt, data_map, hdi)
  lib.calculate_correlationmul(ind.happiness, ind.social_security_contribution, ind.unemployment_rate, data_map, hdi)
  lib.calculate_correlationmul(ind.happiness, ind.social_spending, ind.unemployment_rate, data_map, hdi)

def calculate_correlation_group3(ind, data_map, developed_countries):
  lib.calculate_correlationdiv(ind.happiness, ind.public_debt, ind.gdp_per_capita, data_map, developed_countries)
  lib.calculate_correlationmuldiv(ind.happiness, ind.public_debt, ind.social_security_contribution, ind.gdp_per_capita, data_map, developed_countries)

hdi.selected_countries = { "Germany", "Austria", "Belgium", "Denmark", "Spain", "Finland", "France", "Greece", "Ireland", "Italy", "Luxembourg", "Netherlands", "Portugal", "United Kingdom", "Sweden", "United States" }
ind = Indicators()
data.gdp_per_capita_normalized = lib.normalize_data_minmax(data.gdp_per_capita)
data.hours_worked = lib.extract_latest_from_timeseries(hours_worked.data)
data_map = build_data_map(ind, data, hdi)
#heritage_map = build_heritage_map(Indicators_heritage(), index2023_heritage)
#calculate_correlation_group_gdpadjusted_inv(ind, data_map, hdi)
#calculate_correlation_group_gdp_inv(ind, data_map, hdi)
#calculate_correlation_group_tax_inv(ind, data_map, hdi)
#calculate_correlation_group_life(ind, data_map, hdi)
#calculate_correlation_group_education(ind, data_map, hdi)
#calculate_correlation_group_capitalism(ind, data_map, hdi)
#calculate_correlation_group_socialism(ind, data_map, hdi)
#calculate_correlation_group_system(ind.happiness, data_map, hdi)
#calculate_correlation_group2(ind, data_map, data.developed_countries)
#calculate_correlation_group3(ind, data_map, data.developed_countries)

calculate_correlation_group_indicator(ind.fertility, ind, data_map, hdi)

#time_series_data = lib.TimeSeriesDataGroup("TimeSeriesCategory", hours_worked.hours_worked, 'Hours worked')
#time_series_data.plot_chronological_chart()

#lib.plot_chronological_chart(hours_worked.hours_worked, 'Value')