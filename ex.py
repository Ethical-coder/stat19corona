states=[ 'AN', 'AP', 'AR', 'AS', 'BR', 'CH', 'CT', 'DN', 'DD', 'DL', 'GA','GJ', 'HR', 'HP', 'JK', 'JH', 'KA', 'KL', 'LA', 'LD', 'MP', 'MH', 'MN','ML', 'MZ', 'NL', 'OR', 'PY', 'PB', 'RJ', 'SK', 'TN', 'TG', 'TR', 'UP','UT', 'WB']
statelists=[
'Andaman & Nicobar Islands',
'Andhra Pradesh',
'Arunachal Pradesh',
'Assam',
'Bihar',
'Chandigarh',
'Chhattisgarh',
'Dadar & Nagar Haveli',
'Daman & Diu',
'Delhi',
'Goa',
'Gujrat',
'Haryana',
'Himachal Pradesh',
'Jammu & Kashmir',
'Jharkhand',
'Karnatak',
'Kerela',
'Lakshwadeep',
'Laddakh',
'Madhya Pradesh',
'Maharashtra',
'Manipur',
'Meghalaya',
'Mizoram',
'Nagaland',
'Odisha',
'Pondicherry',
'Punjab',
'Rajasthan',
'Sikkim',
'Tamil Nadu',
'Telangana',
'Tripura',
'Uttar Pradesh',
'Uttarakhand',
'West Bengal'
]

d = dict()

for s in statelists:
    d[s] = states[statelists.index(s)]
print(d)
