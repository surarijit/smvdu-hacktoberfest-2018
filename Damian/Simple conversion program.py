"""Brief and basic beginner program I wrote at the beginning of my learning curve"""

amount_to_convert = 500
nz_to_aus_rate=0.91
nz_dollars=amount_to_convert
converted_aus_dollars= round(amount_to_convert*nz_to_aus_rate , 2)

print("NZD", "to", "AUD")
print()
print("NZD", amount_to_convert , "at",nz_to_aus_rate)
print("=")
print("AUD", round(converted_aus_dollars, 2))
print()
print()

amount_to_convert_1 = 500
aus_to_nz_rate=1/nz_to_aus_rate
aus_dollars=amount_to_convert_1
converted_nz_dollars=amount_to_convert_1*aus_to_nz_rate
print("AUD", "to", "NZD")
print("AUD", amount_to_convert_1, "at" , round(aus_to_nz_rate , 2))
print("=")
print("NZD", round(converted_nz_dollars , 2))

