import pyquotegen

# Get a random quote
quote = pyquotegen.get_quote()
print(quote)

# Get a quote by specific category
quote_by_category = pyquotegen.get_quote("inspirational")
print(quote_by_category)
