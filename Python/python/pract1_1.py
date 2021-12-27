# insert into station (name) VALUES ('Varash');
# insert into station (name) VALUES ('Rafalivka');
# insert into station (name) VALUES ('Antonivka');
# insert into station (name) VALUES ('Sarny');
# insert into station (name) VALUES ('Klesiv');
# insert into station (name) VALUES ('Tomashhorod');
# insert into station (name) VALUES ('Rokytne-Volynske');
# insert into station (name) VALUES ('Ostky');
# insert into station (name) VALUES ('Olevsk');
# insert into station (name) VALUES ('Bilokorovychi');
# insert into station (name) VALUES ('Korosten');
# insert into station (name) VALUES ('Zhytomyr');
# insert into station (name) VALUES ('Fastiv-1');
# insert into station (name) VALUES ('Kyiv-pas');
# insert into station (name) VALUES ('Darnycia');
# insert into station (name) VALUES ('Boryspil');
# insert into station (name) VALUES ('Grebinka');
# insert into station (name) VALUES ('Lubny');
# insert into station (name) VALUES ('Myrgorod');
# insert into station (name) VALUES ('Yaresky');
# insert into station (name) VALUES ('Poltava-Kyivska');
# insert into station (name) VALUES ('Harkiv-pas');
# insert into station (name) VALUES ('Balaklia');
# insert into station (name) VALUES ('Isum');
# insert into station (name) VALUES ('Sviatogirsk');
# insert into station (name) VALUES ('Krasnyy-Lyman');
# insert into station (name) VALUES ('Siversk');
# insert into station (name) VALUES ('Sil');
# insert into station (name) VALUES ('Bahmut');


import datetime

now = datetime.datetime.now() + datetime.timedelta(days=1)

time1 = now.strftime("%Y-%m-%d")
print(time1)

# print("Formatted DateTime:", time1)
