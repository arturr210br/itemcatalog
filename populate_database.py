''' Whole project is based on the Udacity FSND course materials'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Division, User, Base, Driver

engine = create_engine('sqlite:///division.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()
# create sample user
User1 = User(name="Arti Art", email="arturro_88@gmail.com",
             picture='https://www.google.com/url?sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwiCqqDC4_rhAhUeH7kGHRbKCg4QjRx6BAgBEAU&url=https%3A%2F%2Fwww.kodefork.com%2Fusers%2F%3Fpage%3D6&psig=AOvVaw2dHBcuB-ZKLAk8dd6xTC72&ust=1556815402050291')
session.add(User1)
session.commit()

# F1 drivers
f1 = Division(user_id=1, name="Formula 1")

session.add(f1)
session.commit()

driver1 = Driver(user_id=1, name="Lewis Hamilton",
                             description="Lewis Carl Davidson Hamilton MBE (born 7 January 1985) is a British racing driver who races in Formula One for Mercedes-AMG Petronas Motorsport. A five-time Formula One World Champion, he is often considered the best driver of his generation and widely regarded as one of the greatest drivers in the history of the sport.[note 2] He won his first World Championship title with McLaren in 2008, then moved to Mercedes where he won back-to-back titles in 2014 and 2015 before winning back-to-back titles again in 2017 and 2018. The most successful British driver in the history of the sport, Hamilton has more World Championship titles (5) and more race victories (75) than any other British driver in Formula One. He also holds records for the all-time most career points (3,104), the most wins at different circuits (26), the all-time most pole positions (84) and the most grand slams in a season ",
                             rank="1", country="United Kingdom", division=f1)

session.add(driver1)
session.commit()


driver2 = Driver(user_id=1, name="Valtteri Bottas",
                             description="Valtteri Viktor Bottas[2] (born 28 August 1989) is a Finnish racing driver currently competing in Formula One with Mercedes. Bottas previously drove for Williams from 2013 to 2016. He currently resides in Monaco. In his first four races for Mercedes in 2017, Bottas achieved his first Formula One pole position in Bahrain and his first victory at the following event in Russia. He finished the 2017 season taking pole position, fastest lap, and the race win at Abu Dhabi. In 2018 he failed to win a single race for the entire season, becoming the first Mercedes driver since Michael Schumacher in 2012 to not win a race.",
                             rank="2", country="Finland", division=f1)

session.add(driver2)
session.commit()

driver3 = Driver(user_id=1, name="Sebastian Vettel",
                             description="Sebastian Vettel  born 3 July 1987 is a German racing driver who races in Formula One for Scuderia Ferrari.",
                             rank="3", country="Germany", division=f1)

session.add(driver3)
session.commit()

driver4 = Driver(user_id=1, name="Charles Leclerc",
                             description="Charles Leclerc ( born 16 October 1997) is a Monegasque racing driver, currently driving in Formula One for Scuderia Ferrari. Leclerc won the GP3 Series championship in 2016 and the FIA Formula 2 Championship in 2017. Leclerc made his Formula One debut in 2018 for Sauber, a team affiliated with Ferrari, for which he was part of its driver academy. With Sauber having finished last the year before, Leclerc led the charge to improve the finishing position in the constructors' championship to eighth, being the highest ranked of the two Sauber drivers.[3] Leclerc agreed on a contract with Ferrari for the 2019 season where he is driving alongside Sebastian Vettel. Leclerc became the second youngest driver to qualify on pole position in Formula One at the 2019 Bahrain Grand Prix",
                             rank="4", country="Monaco", division=f1)

session.add(driver4)
session.commit()

driver5 = Driver(user_id=1, name="Max Verstappen",
                             description="Max Emilian Verstappen ( born 30 September 1997) is a Belgian-Dutch[2] racing driver who competes under the Dutch flag in Formula One with Red Bull Racing. Aged 17 years, 166 days, he became the youngest driver to compete in Formula 1 at the 2015 Australian Grand Prix. He also holds eight other firsts in Formula One racing. After spending the entire 2015 season with Scuderia Toro Rosso, he started his 2016 campaign with the Italian team, before being promoted into Red Bull Racing mid-season as a replacement for Daniil Kvyat. He won the 2016 Spanish Grand Prix in his debut race for Red Bull Racing at the age of 18, becoming the youngest-ever winner of a Grand Prix and the first racing under the Dutch flag.[3] He is the son of former Formula One driver Jos Verstappen. ",
                             rank="5", country="Netherlands",
                             division=f1)

session.add(driver5)
session.commit()

driver6 = Driver(user_id=1, name="Kimi Raikkonen",
                             description="Kimi-Matias Raikkonen[2] ( born 17 October 1979), nicknamed Iceman, is a Finnish racing driver currently driving in Formula One for Alfa Romeo Racing. He won the 2007 Formula One World Championship, in his first season at Scuderia Ferrari. After nine seasons racing in Formula One, he competed in the World Rally Championship in 2010 and 2011, then returning to Formula One from 2012. Besides his title, Raikkonen also finished second overall in 2003 and 2005 and third in 2008, 2012 and 2018. Prior to the 2019 season, Raikkonen has won 21 Grands Prix, making him the Finnish Formula One driver with the most race wins. He is the only driver to take a race win in the V10, V8 and the hybrid V6 engine eras",
                             rank="6", country="Finland", division=f1)

session.add(driver6)
session.commit()

driver7 = Driver(user_id=1, name="Antonio Giovinazzi",
                             description="Antonio Giovinazzi (born 14 December 1993) is an Italian racing driver currently competing in Formula One for Alfa Romeo Racing. He was the 2015 FIA Formula 3 European Championship runner-up and raced with Prema in the 2016 International GP2 Series, again finishing runner-up with five wins and eight overall podiums. Giovinazzi was chosen by Scuderia Ferrari to be their third and reserve driver for the 2017 season. He made his competitive debut for Sauber at the 2017 Australian Grand Prix, replacing the injured Pascal Wehrlein. He also replaced Wehrlein at the following Chinese Grand Prix as Wehrlein continued his recovery.[2] Giovinazzi signed a contract to race full-time for Alfa Romeo Racing in 2019. ",
                             rank="7", country="Italy", division=f1)

session.add(driver7)
session.commit()

driver8 = Driver(user_id=1, name="Pierre Gasly",
                             description="Pierre Gasly ( born 7 February 1996) is a French racing driver, currently racing in Formula One for Red Bull Racing. He was the 2016 GP2 Series champion, and the runner-up in the 2014 Formula Renault 3.5 Series and the 2017 Super Formula Championship. He made his Formula One debut at the 2017 Malaysian Grand Prix.[2] He began with Red Bull Racing in 2019",
                             rank="8", country="France", division=f1)

session.add(driver8)
session.commit()

driver9 = Driver(user_id=1, name="Robert Kubica",
                             description="Robert Jozef Kubica  ( born 7 December 1984) is a Polish racing driver who is currently racing for the Williams F1 team. He became the first Polish driver to compete in Formula One. Between 2006 and 2009 he drove for the BMW Sauber F1 team, promoted from test driver to race driver during 2006. In June 2008, Kubica took his maiden Formula One victory in the Canadian Grand Prix, becoming the first Polish driver to win a Formula One race. That season he led the championship at one stage, before finishing fourth overall, his best career position. Kubica drove for Renault in 2010 and was set to remain with the team in 2011. Several years later Kubica confirmed he had signed a pre-contract for the 2012 season with Ferrari, a move that was eventually cancelled by his devastating rally crash in the winter of 2011",
                             rank="9", country="Poland", division=f1)

session.add(driver9)
session.commit()

driver10 = Driver(user_id=1, name="George Russell",
                             description="George Russell (born 15 February 1998) is a British racing driver currently competing in the 2019 Formula One World Championship for the Williams team. He is the reigning FIA Formula 2 Champion for ART and the 2017 GP3 Series Champion. ",
                             rank="10", country="United Kingdom", division=f1)

session.add(driver10)
session.commit()

# F2 drivers
f2 = Division(user_id=1, name="Formula 2")

session.add(f2)
session.commit()


driver1 = Driver(user_id=1, name="Nicholas Latifi",
                             description="Nicholas Latifi (born in Montreal, Quebec, Canada[1] on 29 June 1995) is a Canadian racing driver, formerly serving as Racing Point Force India's F1 development driver and in 2019 became Williams' test and reserve driver.[2] ",
                             rank="1", country="Canada", division=f2)

session.add(driver1)
session.commit()


driver2 = Driver(user_id=1, name="Jack Aitken",
                             description="Jack Aitken (born 23 September 1995) is a British-Korean[1] racing driver currently competing in Formula 2 for Campos Racing.[2] Aitken began his career in Karting at Buckmore Park, aged 7. He made the transition to cars when he competed in the Intersteps Championship with Fortec Motorsport, with whom he then went on to race with in the Formula Renault BARC Winter Series, Formula Renault NEC and Formula Renault Eurocup. ",
                             rank="2", country="United Kingdom", division=f2)

session.add(driver2)
session.commit()

driver3 = Driver(user_id=1, name="Luca Ghiotto",
                             description="Luca Ghiotto (born 24 February 1995) is an Italian racing driver currently competing in Formula 2 for UNI-Virtuosi Racing. ",
                             rank="3", country="Italy", division=f2)

session.add(driver3)
session.commit()

driver4 = Driver(user_id=1, name="Nyck de Vries",
                             description="Nyck de Vries (born 6 February 1995 in Sneek)[1][2] is a Dutch racing driver currently competing in Formula 2 for ART Grand Prix. He won the 2010 and 2011 Karting World Championships and in 2014 the Formula Renault 2.0 Alps and Formula Renault 2.0 Eurocup Championships. He used to be managed by Anthony Hamilton (father of Lewis Hamilton)[3] and was signed to the McLaren young driver programme in January 2010 and Audi Sport racing academy in 2017",
                             rank="4", country="Netherlands", division=f2)

session.add(driver4)
session.commit()

driver5 = Driver(user_id=1, name="Sergio Sette Camara",
                             description="Sergio Sette Camara Filho (born 23 May 1998) is a Brazilian racing driver currently competing in Formula 2, for DAMS. He is a former member of the Red Bull Junior Team.[1] he is test and development driver for McLaren. ",
                             rank="5", country="Brazil",
                             division=f2)

session.add(driver5)
session.commit()

driver6 = Driver(user_id=1, name="Juan Manuel Correa",
                             description="Juan Manuel Correa (born August 9, 1999) is an Ecuadorian-American racing driver who competes with Prema Powerteam in the Italian F4 and ADAC Formula 4 championships.",
                             rank="6", country="United States of America", division=f2)

session.add(driver6)
session.commit()

driver7 = Driver(user_id=1, name="Jordan King",
                             description="Jordan King (born 26 February 1994 in Warwick) is a British racing driver from Harbury, Warwickshire. He currently competes in the FIA Formula 2 Championship with the team MP Motorsport. ",
                             rank="7", country="United Kingdom", division=f2)

session.add(driver7)
session.commit()

driver8 = Driver(user_id=1, name="Louis Deletraz",
                             description="Louis Deletraz (born 22 April 1997) is a Swiss racing driver currently competing in Formula 2 for Carlin. He is the son of former Formula One and Le Mans 24 Hours driver Jean-Denis Deletraz",
                             rank="8", country="Switzerland", division=f2)

session.add(driver8)
session.commit()

driver9 = Driver(user_id=1, name="Mick Schumacher",
                             description="Mick Schumacher ( born 22 March 1999)[1][2] is a German racing driver, currently competing in the FIA Formula 2 Championship with Prema Theodore Racing and being affiliated to the Ferrari Driver Academy.[3] He began his career in karting in 2008, progressing to the German ADAC Formula 4 by 2015. Mick most recently competed in the 2018 FIA F3 European Championship, which he won. He is the son of seven-time Formula One World Champion Michael Schumacher, nephew of former Formula One driver Ralf Schumacher, and stepnephew of Sebastian Stahl.",
                             rank="9", country="Germany", division=f2)

session.add(driver9)
session.commit()

driver10 = Driver(user_id=1, name="Anthoine Hubert",
                             description="Anthoine Hubert (born 22 September 1996) is a French professional racing driver. He is the 2018 GP3 Series champion. ",
                             rank="10", country="France", division=f2)

session.add(driver10)
session.commit()


# F3 drivers
f3 = Division(user_id=1, name="Formula 3")

session.add(f3)
session.commit()


driver1 = Driver(user_id=1, name="Marcus Armstrong",
                             description="Marcus Armstrong (born 29 July 2000), is a New Zealand motor racing driver, who most recently competed in the 2018 FIA F3 European Championship for Prema Powerteam under the Italian flag",
                             rank="1", country="New Zealand", division=f3)

session.add(driver1)
session.commit()


driver2 = Driver(user_id=1, name="Jehan Daruvala",
                             description="Jehan Daruvala (born 1 October 1998) is an Indian racing driver, currently competing in the European Formula 3 Championship with Prema Powerteam. He is a protege of the Racing Point Force India F1 team, after being one of three winners of a 'One in a Billion hunt' organized by the team in 2011",
                             rank="2", country="India", division=f3)

session.add(driver2)
session.commit()

driver3 = Driver(user_id=1, name="Robert Shwartzman",
                             description="Robert Mikhailovich Shwartzman ( born 16 September 1999) is a Russian racing driver currently competing in the European Formula 3 Championship. He is a member of the Ferrari Driver Academy.[1] He is the 2018 Toyota Racing Series champion",
                             rank="3", country="Russia", division=f3)

session.add(driver3)
session.commit()

driver4 = Driver(user_id=1, name="Teppei Natori",
                             description="Teppei Natori (born 11 September 2000) is a Japanese racing driver backed by Honda",
                             rank="4", country="Japan", division=f3)

session.add(driver4)
session.commit()

driver5 = Driver(user_id=1, name="Felipe Drugovich",
                             description="Felipe Drugovich Roncato (born 23 May 2000 in Maringa) is a Brazilian racing driver.  ",
                             rank="5", country="Brazil",
                             division=f3)

session.add(driver5)
session.commit()

driver6 = Driver(user_id=1, name="Logan Sargeant",
                             description="Logan Hunter Sargeant (born December 31, 2000 in Boca Raton) is an American racing driver. ",
                             rank="6", country="United States of America", division=f3)

session.add(driver6)
session.commit()

driver7 = Driver(user_id=1, name="Leonardo Pulcini",
                             description="Leonardo Pulcini (born 25 June 1998 in Rome) is an Italian racing driver and the 2016 Euroformula Open champion",
                             rank="7", country="Italy", division=f3)

session.add(driver7)
session.commit()

driver8 = Driver(user_id=1, name="Juri Vips",
                             description="Juri Vips (born 10 August 2000) is an Estonian racing driver, 2017 ADAC Formula 4 champion and member of the Red Bull Junior Team.",
                             rank="8", country="Estonia", division=f3)

session.add(driver8)
session.commit()

driver9 = Driver(user_id=1, name="Ye Yifei",
                             description="Ye Yifei ( born 16 June 2000) is a Chinese racing driver, 2016 French F4 champion and member of the Renault Sport Academy.",
                             rank="9", country="China", division=f3)

session.add(driver9)
session.commit()

driver10 = Driver(user_id=1, name="David Beckmann",
                             description="David Beckmann (born 27 April 2000) is a German racing driver. ",
                             rank="10", country="Germany", division=f3)

session.add(driver10)
session.commit()



# WRC drivers
wrc = Division(user_id=1, name="WRC- World Rally Championship")

session.add(f3)
session.commit()


driver1 = Driver(user_id=1, name="Thierry Neuville",
                             description="Thierry Jean Neuville (born 16 June 1988) is a Belgian rally driver, he is currently competing in the World Rally Championship. His co-driver was Nicolas Klinger from his debut until the end of 2010. Klinger was replaced by Nicolas Gilsoul for the first 2011 IRC rally, Monte Carlo. Since 2014, Neuville and Gilsoul have driven a factory-backed Hyundai i20 WRC for Hyundai Motorsport.[1] He has finished as runner-up in the World Rally Championship four times, in 2013, 2016, 2017 and 2018. ",
                             rank="1", country="Belgium", division=wrc)

session.add(driver1)
session.commit()


driver2 = Driver(user_id=1, name="Sebastien Ogier",
                             description="Sebastien Ogier (born 17 December 1983) is a French rally driver, competing for Citroen in the World Rally Championship (WRC), who is teamed with co-driver Julien Ingrassia. He is the current holder of the World Rally Drivers' Championship, having won the title six times, in 2013, 2014, 2015, 2016, 2017 and 2018. With 46 victories in the World Rally Championship and 6 consecutive WRC titles, he is the 2nd most successful WRC driver, after former Citroen WRC teammate Sebastien Loeb (9 titles). ",
                             rank="2", country="France", division=wrc)

session.add(driver2)
session.commit()

driver3 = Driver(user_id=1, name="Ott Tanak",
                             description="Ott Tanak (born 15 October 1987) is an Estonian rally driver. He is currently teamed with Martin Jarveoja and is competing for Toyota in the World Rally Championship. In the 2017 and 2018 seasons, Tanak and Jarveoja finished 3rd in the overall driver's standings, behind rivals Thierry Neuville and Sebastien Ogier. At 7 WRC event wins, Ott Tanak is the most successful Estonian rally driver, surpassing previous best Markko Martin, who retired with 5 event wins. ",
                             rank="3", country="Estonia", division=wrc)

session.add(driver3)
session.commit()

driver4 = Driver(user_id=1, name="Kris Meeke",
                             description="Kris Meeke (born 2 July 1979) is a Northern Irish professional rally driver, best known for competing in the FIA World Rally Championship (WRC). He was the 2009 Intercontinental Rally Challenge champion. His co-driver is United Kingdoms Seb Marshall.[1] He began his career as a Computer Aided Designer with M-Sport, at the headquarters of the Ford World Rally Team, before moving on to competing in the Peugeot Super 106 Cup in 2001.[2] ",
                             rank="4", country="Northern Ireland, UK", division=wrc)

session.add(driver4)
session.commit()

driver5 = Driver(user_id=1, name="Elfyn Evans",
                             description="Elfyn Rhys Evans (born 28 December 1988) is a British rally driver from Wales who competes in the World Rally Championship. ",
                             rank="5", country="Wales, UK",
                             division=wrc)

session.add(driver5)
session.commit()

driver6 = Driver(user_id=1, name="Andreas Mikkelsen",
                             description="Andreas Mikkelsen (born 22 June 1989) is a Norwegian rally driver. He drove a factory Volkswagen Polo R WRC in the World Rally Championship from 2013 to 2016. He finished third in the drivers standings in 2014, 2015 and 2016, collecting three wins and 20 podiums. He currently drives for Hyundai. ",
                             rank="6", country="Norway", division=wrc)

session.add(driver6)
session.commit()

driver7 = Driver(user_id=1, name="Jari-Matti Latvala",
                             description="Jari-Matti Latvala (born 3 April 1985) is a Finnish rally driver competing in the World Rally Championship (WRC). His co-driver has been Miikka Anttila since the 2003 Rallye Deutschland. He is well known for his aggressive driving style, which earns him many plaudits, and comparisons to the late Colin McRae. With 18 event victories in the WRC, he is the most successful driver to not have won a championship. Latvala is also the driver with the most World Rally starts in the sport which he achieved in 2019, 17 years after his debut. ",
                             rank="7", country="Finland", division=wrc)

session.add(driver7)
session.commit()

driver8 = Driver(user_id=1, name="Esapekka Lappi",
                             description="Esapekka Lappi (born 17 January 1991) is a Finnish rally driver. He is the 2012 Finnish Rally Champion, 2014 European Rally Champion and the 2016 WRC-2 Champion. He is currently competing for Citroen Total WRT in the World Rally Championship. ",
                             rank="8", country="Finland", division=wrc)

session.add(driver8)
session.commit()

driver9 = Driver(user_id=1, name="Dani Sordo",
                             description="Daniel   Sordo Castillo (born 2 May 1983) is a Spanish rally driver. He competes in the World Rally Championship for Hyundai Motorsport. He achieved his first WRC victory at the 2013 Rallye Deutschland. ",
                             rank="9", country="Spain", division=wrc)

session.add(driver9)
session.commit()

driver10 = Driver(user_id=1, name="Sebastien Loeb",
                             description="Sebastien Loeb ( born 26 February 1974) is a French professional rally, racing, and rallycross driver. He competed for the Citroen World Rally Team in the World Rally Championship (WRC) and is the most successful driver in WRC history, having won the world championship a record nine times in a row. He holds several other WRC records, including most event wins, most podium finishes and most stage wins. Loeb announced his retirement from World Rallying at the end of the 2012 season. Participating in selected events in the 2013 WRC season, he raced a full season in the FIA GT Series driving a McLaren MP4-12C before moving on with Citroen to the FIA World Touring Car Championship in 2014. In the 2018 season he is one of the official drivers of the Team Peugeot Total.[1] ",
                             rank="10", country="France", division=wrc)

session.add(driver10)
session.commit()


print "Added divisions and drivers ."
