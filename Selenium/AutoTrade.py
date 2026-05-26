import yfinance
import selenium
from selenium import webdriver
dat = yfinance.Ticker("MSFT")
dat.info
dat.calendar
dat.analyst_price_targets
dat.quarterly_income_stmt
dat.history(period='1mo')
dat.option_chain(dat.options[0]).calls

print(dat.earnings_estimate)

