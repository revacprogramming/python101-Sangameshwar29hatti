text = "X-DSPAM-Confidence: 0.8475";
z =text.find('0.8475')
number = text[z::1]
print(float(number))