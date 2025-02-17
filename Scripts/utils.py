company_name = ['Honda', 'Suzuki', 'Toyota', 'Daihatsu', 'Changan', 'Subaru',
       'Nissan', 'Hyundai', 'KIA', 'MG', 'DFSK', 'Mitsubishi', 'Datsun',
       'Mercedes', 'Jeep', 'Audi', 'Range', 'BMW', 'Peugeot', 'SsangYong',
       'Adam', 'Proton', 'Haval', 'Mazda', 'FAW', 'Chery', 'Lexus',
       'Prince', 'Chevrolet', 'BAIC', 'Porsche', 'Ford', 'Daewoo',
       'Others', 'Land', 'United', 'Isuzu', 'Volkswagen', 'MINI', 'Tesla',
       'Fiat', 'JMC', 'Power', 'JW', 'Master', 'Willys', 'Dodge', 'GMC',
       'Daehan', 'Cadillac', 'Jaguar', 'JAC', 'ORA', 'Tank', 'Buick',
       'Alfa', 'Rinco', 'Seres', 'Sogo', 'GUGO', 'Chrysler', 'Hino',
       'Vauxhall', 'Genesis', 'Volvo', 'Hummer', 'ZOTYE']


car_models = ['Vezel ', 'Wagon R', 'Corolla Axio', 'Corolla ', 'Mira ',
       'Alsvin ', 'BR-V ', 'Civic ', 'Civic Eagle', 'City ', 'Cultus ',
       'Prado ', 'Fortuner ', 'Dex ', 'Passo ', 'Aqua ', 'Dayz ', 'Alto ',
       'Santro ', 'Raize ', 'Sportage ', 'N One', 'Vitz ', 'HS ', 'N Wgn',
       'Glory 580', 'City 5th', 'Note ', 'EK X', 'Ravi ', 'Tanto ',
       'Yaris ', 'Land Cruiser', 'Cuore ', 'Mehran ', 'Estima ', 'Leaf ',
       'C-HR ', 'Corolla Hybrid', 'Yaris Hatchback', 'Swift ',
       'Corolla Fielder', 'Surf ', 'Khyber ', 'Civic Reborn', '120 Y',
       'Benz C', 'Crown ', 'City 6th', 'Stonic ', 'Civic Rebirth',
       'Bolan ', 'Elantra ', 'Hilux ', 'HR-V ', 'CJ 5', 'A4 4th',
       'Rover Vogue', 'Camry ', 'Insight ', 'Corolla Indus',
       'Yaris Cross', 'Cast ', 'iX ', 'Prado 90', 'Tucson ', 'Accord ',
       'Cefiro ', 'Premio ', 'Platz ', 'Move ', 'Sonata ', '7 Series',
       'March ', 'Hijet ', 'A4 ', 'Rush ', 'Moco ', 'Liana ', 'Ek Wagon',
       'Hustler ', 'Civic 11th', 'Every ', '2008 ', '3 Series', 'Baleno ',
       'Dayz Highway', 'Sunny ', 'Prius ', 'Rexton ', 'Revo ', 'Karvaan ',
       'X70 ', 'Prado 120', 'Taft ', 'H6 ', 'Picanto ', 'Corolla 9th',
       'e-tron ', 'Pleo ', 'Carol ', 'Charade ', 'Fit ', 'Flair ',
       'Rocky ', 'Stella ', 'Kicks ', 'V2 ', 'Benz E', 'N Box', 'Copen ',
       'Tiggo 8', 'Carrier ', 'Belta ', 'LX Series', 'A6 4th', 'Benz S',
       'Pearl ', 'A5 ', 'Rav4 ', 'Freed ', 'Sorento ', 'Otti ', '626 ',
       'Camry XV50', 'Sienta ', 'Corolla Cross', 'Raum ', 'Pajero ',
       'Voxy ', 'Other ', 'Margalla ', 'Pixis Epoch', 'Life ', 'APV ',
       'A3 ', 'Every 11th', 'Serena ', 'Lancer ', 'Civic EK',
       'Terios Kid', 'Hiace ', 'Optra ', 'Jimny ', 'Saga ', 'RX Series',
       'Prius Alpha', 'Every Wagon', 'Joy ', 'BJ40 Plus', '911 ', 'Thor ',
       'Clipper ', 'Mustang ', 'Oshan X7', 'EK Space', 'Spacia ',
       'Mark X', 'Kei ', 'Racer ', 'ZS EV', 'Esquire ', 'Santa Fe',
       'Allion ', 'Verisa ', 'Ciaz ', 'Taycan ', 'Tundra ', 'F 150',
       'X1 ', 'Boon ', 'i7 ', '4 ', 'Town Ace', 'Benz EQC', 'K07 ',
       'Rover Defender', 'Pajero Junior', 'Navara ', 'AD Van', 'Roox ',
       'Alto Lapin', 'ZS ', 'Juke ', 'L200 ', 'Panamera ',
       'Bluebird Sylphy', 'Skyline ', 'Exclusive ', 'Rover Sport',
       'Roomy ', 'Jolion ', 'Minica ', 'Bravo ', 'RX8 ', 'Camry XV70',
       'Kaghan XL', 'Benz EQS', 'D-Max ', 'Wrangler ', 'X-PV ',
       '5 Series', 'Noah ', 'Harrier ', 'Storia ', 'CR-V ', 'Beetle Foxy',
       'Cooper ', 'Model 3', 'e-tron GT', 'Patrol ', 'FX ', 'ISIS ',
       'M Series', 'Potohar ', 'Alphard ', 'Sirius ', 'EK Custom',
       'Benz EQE', 'Benz G', 'BJ40 ', 'Spike ', 'NKR ', 'Pajero Mini',
       'Mark II', 'Esse ', 'A6 ', 'Wingroad ', 'Spectra ', 'Tiggo 4',
       'Clarity ', 'Coupe ', 'Grace Hybrid', 'X6 Series',
       'Grand Carnival', 'Civic EG', 'Stavic ', 'Trooper ', 'Atrai Wagon',
       'K01 ', 'Vigus ', 'Move Conte', 'Shehzore ', 'Excel ',
       'Camry XV40', 'Supra ', 'Cervo ', 'Avanza ', 'CR-Z Sports',
       'Xbee ', 'Classic ', 'Model X', 'Benz Brabus', 'Cayenne ', 'Duet ',
       ' Mini', 'Corona ', 'Starlet ', 'X5 Series', 'Avensis ', 'Scrum ',
       'Forland Bravo', 'Airwave ', 'Toppo ', 'Alphard V', 'Mira Cocoa',
       'GS ', 'Move Canbus', 'Tiida ', 'Terios ', '86 ', 'Vitara ', 'Nx ',
       'Fj Cruiser', 'Sylphy ', 'Vamos ', 'Benz M', 'Benz CLK', 'Kix ',
       'Galant ', 'Aygo ', 'M9 ', 'Kona ', 'Sambar ', 'Rvr ', 'Mirage ',
       'Samurai ', 'Wish ', 'X2 ', 'Rover Discovery', 'IST ',
       'Corolla Hatchback', 'Rx7 ', 'Scrum 11th', '5 ', 'MX 5', 'CT200h ',
       'M8 ', 'Carry ', 'MR Wagon', 'Q3 ', 'Foton ', 'Lafesta ',
       'Benz GLS', 'Beetle ', 'M38 ', 'Bego ', 'Porte ', 'Acty ',
       'Kizashi ', 'Benz GLA', 'Sprinter ', 'Charger ', 'Benz 200', 'I ',
       'Probox ', 'Sierra ', 'S660 ', 'Wake ', 'Vellfire ', 'Niro ',
       'Cross Road', 'Stream ', 'Escalade Ext', 'M 151', 'Jade ',
       'Camaro ', 'Nv350 Caravan', 'Challenger ', 'Sakura ', 'Tank ',
       'Accord Tourer', 'Sonica ', 'Safari ', 'Impreza ', 'X200 ',
       'Cami ', 'Cressida ', 'Titan ', 'Note Aura', 'Splash ',
       'Gladiator ', '03 ', '500 ', '370Z ', 'Pino ', 'Spark ', 'Almera ',
       '5 EV', 'Benz GLB', 'Mustang Mach-E', 'Brz ', '1200 ', 'Ractis ',
       'Qashqai ', 'Cruze ', 'Century ', 'Alphard G', 'Cielo ',
       'Coaster ', 'Model S', 'Romeo Other', 'Axela ', 'Benz SLK',
       'Aria ', 'Van ', 'iX3 ', 'Transporter T6', 'Tacoma ', 'Q7 ',
       'Ram ', 'UX ', '3 ', 'Carina ', 'Forland Safari', 'E-2008 ', 'Q5 ',
       'Fit Aria', 'Pickup ', '323 ', 'Allex ', 'Pride ', 'Corvette ',
       'Forland C-10', 'iQ ', 'Q2 1st', 'Alpha ', 'Benz CLA', 'Benz X',
       'Bronco ', 'Sc ', '350Z ', 'GIGI ', 'Infinity ', 'Cherokee ',
       'Jimny Sierra', 'L300 ', 'Macan ', 'Ranger ', 'X Trail',
       'Caravan ', 'Chaser ', 'Murano ', 'A8 ', 'Coo ', 'Grandis ',
       'S Cross', 'R2 ', 'Zest ', 'Grand Starex', '300 C', 'Sx4 ',
       'Micra ', 'QQ ', 'Gilgit ', 'Grace ', 'Mega Carry', 'Uno ',
       'Minicab Bravo', 'Inspire ', 'Cts ', 'Benz Smart', 'Z3 ',
       'Caprice ', 'i8 ', 'Kluger ', 'Q2 ', 'Stinger ', 'Cappuccino ',
       'XF ', 'H-100 ', 'Flair Crossover', 'Bezza ', 'X3 Series',
       'Clipper 11th', 'Celerio ', 'Blue Bird', 'Rover Autobiography',
       '808 ', 'Lucida ', 'Rio ', 'Vamos Hobio', 'Pixo ', 'Roadmaster ',
       'Succeed ', 'Lancer Evolution', 'Sj410 ', 'Gen 2', 'Cx3 ',
       'Verossa ', 'Terracan ', 'TT ', 'i10 ', 'i4 ', 'Move Latte',
       'Xenia ', '500 Series', 'Biante ', 'Lesabre ', 'Rumion ', 'Benz A',
       'Pony ', 'Accent ', 'Charmant ', 'Iveco ', 'Sera ', 'Mighty ',
       'Aveo ', '124 ', 'Pixis Space', 'Sentra ', 'LS Series', 'Demio ',
       'A7 ', 'Thats ', 'GV60 ', 'Dyna ', 'CX70T ', 'Cr X', '206 ',
       'Celica ', 'Z4 ', '1 Series', 'C37 ', 'Palette ', 'Solio ', 'V40 ',
       'Forland C-19', '1000 ', 'Path Finder', 'Outlander ', 'Mira Gino',
       'Crown Victoria', 'Carol Eco', 'Acura ', 'FUSO ', 'Cj 7',
       'Benz Sprinter', 'Shahbaz ', 'XC90 ', 'Beat ', 'Pulsar ',
       'Corolla Assista', 'ES ', 'Integra ', 'H3 ', 'S90 ', 'Cima ',
       'Scrum Wagon', 'Benz CLS', 'Z100 ', 'Model Y', 'Mutt M', 'Tercel ',
       '2 Series', 'R1 ', 'Today ', 'Rover Series']