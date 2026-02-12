# Name : Abigail Wangechi
# Date : 12/2/2026
# String formating

# Get string length
sentence = "I watch anime"

string_length = len(sentence)

print(f"The lenghth is : {string_length}")

# Splitting a string
sentence_2 = "Mathematics Physics"
split = sentence_2.split(" ")

print(f"the first subject is:",split[0])

# Make everything CAPS
mpesa_code = "ub34kjus"

capitalized = mpesa_code.upper()

print(f"New mpesa code:",capitalized)

# Make evrything lowercase
mpesa_code = "UB67OKLISH"

lowercase = mpesa_code.lower()

print(f"New mpesa code :",lowercase)

balance = "100Kes"
amount_added = "50Kes"

cleaned_balance = balance.replace("Kes","")

print(f"cleaned_balance:",cleaned_balance)

cleaned_amount_added = amount_added.replace("Kes","")

print(f"cleaned_amount_added:{cleaned_amount_added}")

final_balance = int(cleaned_balance) + int(cleaned_amount_added)

print(f"the final balance is :{final_balance}")

sentence_3 = "CONFIRMED you have received 40Kes from Phillip"
split = sentence_3.split(" ")

print(f"the amount is:",split[4])

amount = "40Kes"
final_amount = amount.replace("Kes"," ")

print(f"final_amount:",final_amount)



