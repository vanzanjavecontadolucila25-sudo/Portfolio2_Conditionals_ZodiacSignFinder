##Read Me: In fulfillment for the subject BES 10a, this project is a Python-based Zodiac Sign Finder that gives users' their respective zodiac signs based on their birth month and birth date. It demonstrates basic programming concepts such as user input and print functions for interaction, type conversion for data processing, and try/except blocks for error validation. The code features multi-way decisions using if, elif, and else structures alongside nested decisions to categorize birth dates, while utilizing proper indentation and comparison operators to ensure precise logic throughout the project.

#The informations used in classifying zodiac signs was acquired from allure.com 
#source link: https://www.allure.com/story/zodiac-sign-personality-traits-dates

##This is the title section##
print ('=========================Zodiac Sign Finder=========================')
print ("Every sign brings something to the celestial table. Here's what you")
print ('should know about the zodiac signs, including strengths, weaknesses,')
print ('and how they think. Discover your own Zodiac Sign now!')

##For any section in the page containing "print ('')", expect it to be a page break/space##
print ('')        

#The birth month of the users' are acquired using:
print ('Note: Input only english alphabet letters and with no punctuations.')
month=input('Input your birth month:')

##This part uses try/except statements to validate users' inputs
#try statement only accepts integer, if the input cannot be converted to int (for an input is a str), the error will not print
#if try is true (for an input is an integer), the error will be displayed
try:
    int(month)
    print ('')
    print('ERROR: Input must contain letters only.')
    
#when try statement is false, except will run with its nested statements
except:
    print('')
    ##if the string input is "January" (with limited three variations since it is case sensitive) the following occurs
    #use of 'or' operator from geeksforgeeks.org
    #source link: https://www.geeksforgeeks.org/python/python-or-operator/
    if month=='January' or month=='JANUARY' or month=='january':
        print ('Note: Input only numerical values.')
        #the system will require the user' birthdate to narrow down the sorting of category of zodiac sign
        birthdate= input('Input your birthday:')
        #this ensures that the user will input ONLY integers
        try:
            bval= int(birthdate)
        #except will be true if the input is not an integer (class is string)
        except:
            bval= -1
        #when the date input is within the range of the maximum date of the month, the ff will occur to select the—
        #zodiac signs for the month of January within the set of dates for specific zodiac
        if bval>0:
            print ('')
            if bval >=1:
                if bval <=19:
                    print ('====================================================================')
                    print ('Your zodiac sign is:')
                    print ('                            Capricorn')
                    print ('What is the most valuable resource? For Capricorn, the answer is')
                    print ('clear: time. Capricorn is climbing the mountain straight to the top')
                    print ('and knows that patience, perseverance, and dedication are the only')
                    print ('way to scale. Capricorn, the last earth sign of the zodiac, is')
                    print ('represented by the sea goat, a mythological creature with the body')
                    print ('of a goat and the tail of a fish. Accordingly, Capricorns are')
                    print ('skilled at navigating both the material and emotional realms.')
                    print ('====================================================================')
                if bval >=20:
                    if bval <=31:
                        print ('====================================================================')
                        print ('Your zodiac sign is:')
                        print ('                            Aquarius')
                        print ('Despite the "aqua" in its name, Aquarius is actually the last air')
                        print ('sign of the zodiac. Innovative, progressive, and shamelessly')
                        print ('revolutionary, Aquarius is represented by the water bearer, the')
                        print ('mystical healer who bestows water, or life, upon the land.') 
                        print ('Accordingly, Aquarius is the most humanitarian astrological sign.')
                        print ('At the end of the day, Aquarius is dedicated to making the world a')
                        print ('better place.')
                        print ('====================================================================')
                #this ensures that the range for the the date that users' can input is within the maximum date of the—
                #month, otherwise display error
                if bval>31:
                        print ('EROR: Invalid date value for January.') 
        #when the input is 0, negative, or a string (except is true), it prints an error
        else:
            print ('')
            print ('ERROR: Input is not a number or input is not a valid date for January.')
 ##For instances that the month is not January (false), then the program will run any of the following that applies
 #note that the same mechanism applies (refer to January) in narrowing down the choices, just with different month— 
 #and with different set or categories of Zodiac Signs
    elif month=='February' or month=='FEBRUARY' or month=='february':
        print ('Note: Input only numerical values.')
        birthdate= input('Input your birthday:')
        try:
            bval= int(birthdate)
        except:
            bval= -1
        if bval>0:
            print ('')
            if bval >=1:
                if bval <=18:
                    print ('====================================================================')
                    print ('Your zodiac sign is:')
                    print ('                            Aquarius')
                    print ('Despite the "aqua" in its name, Aquarius is actually the last air')
                    print ('sign of the zodiac. Innovative, progressive, and shamelessly')
                    print ('revolutionary, Aquarius is represented by the water bearer, the')
                    print ('mystical healer who bestows water, or life, upon the land.') 
                    print ('Accordingly, Aquarius is the most humanitarian astrological sign.')
                    print ('At the end of the day, Aquarius is dedicated to making the world a')
                    print ('better place.')
                    print ('====================================================================')
                if bval >=19:
                    if bval <=29:
                        print ('====================================================================')
                        print ('Your zodiac sign is:')
                        print ('                            Pisces')
                        print ('If you looked up the word "psychic" in the dictionary, there would')
                        print ('definitely be a picture of Pisces next to it. Pisces is the most')
                        print ('intuitive, sensitive, and empathetic sign of the entire zodiac—and')
                        print ('that’s because it’s the last of the last. As the final sign, Pisces')
                        print ('has absorbed every lesson—the joys and the pain, the hopes and the')
                        print ("fears—learned by all the other signs. It's symbolized by two fish")
                        print ('swimming in opposite directions, representing the constant division')
                        print ("of Pisces' attention between fantasy and reality.")
                        print ('====================================================================')
                #The maximum date for month of february is 29
                if bval>29:
                        print ('EROR: Invalid date value for February.') 
        else:
            print ('')
            print ('ERROR: Input is not a number or input is not a valid date for February.')
    elif month=='March' or month=='MARCH' or month=='march':
        print ('Note: Input only numerical values.')
        birthdate= input('Input your birthday:')
        try:
            bval= int(birthdate)
        except:
            bval= -1
        if bval>0:
            print ('')
            if bval >=1:
                if bval <=20:
                    print ('====================================================================')
                    print ('Your zodiac sign is:')
                    print ('                            Pisces')
                    print ('If you looked up the word "psychic" in the dictionary, there would')
                    print ('definitely be a picture of Pisces next to it. Pisces is the most')
                    print ('intuitive, sensitive, and empathetic sign of the entire zodiac—and')
                    print ('that’s because it’s the last of the last. As the final sign, Pisces')
                    print ('has absorbed every lesson—the joys and the pain, the hopes and the')
                    print ("fears—learned by all the other signs. It's symbolized by two fish")
                    print ('swimming in opposite directions, representing the constant division')
                    print ("of Pisces' attention between fantasy and reality.")
                    print ('====================================================================')
                if bval >=21:
                    if bval <=31:
                        print ('====================================================================')
                        print ('Your zodiac sign is:')
                        print ('                            Aries')
                        print ('The first sign of the zodiac, Aries loves to be number one.')
                        print ('Naturally, this dynamic fire sign is no stranger to competition.')
                        print ('Bold and ambitious, Aries dives headfirst into even the most')
                        print ("challenging situations—and they'll make sure they always come out")
                        print ('on top.')
                        print ('====================================================================')
                if bval>31:
                        print ('EROR: Invalid date value for March.') 
        else:
            print ('')
            print ('ERROR: Input is not a number or input is not a valid date for March.')
    elif month=='April' or month=='APRIL' or month=='april':
        print ('Note: Input only numerical values.')
        birthdate= input('Input your birthday:')
        try:
            bval= int(birthdate)
        except:
            bval= -1
        if bval>0:
            print ('')
            if bval >=1:
                if bval <=19:
                    print ('====================================================================')
                    print ('Your zodiac sign is:')
                    print ('                            Aries')
                    print ('The first sign of the zodiac, Aries loves to be number one.')
                    print ('Naturally, this dynamic fire sign is no stranger to competition.')
                    print ('Bold and ambitious, Aries dives headfirst into even the most')
                    print ("challenging situations—and they'll make sure they always come out")
                    print ('on top.')
                    print ('====================================================================')
                if bval >=20:
                    if bval <=31:
                        print ('====================================================================')
                        print ('Your zodiac sign is:')
                        print ('                            Taurus')
                        print ('What sign is more likely to take a six-hour bath followed by a')
                        print ('luxurious Swedish massage and decadent dessert spread? Why Taurus,')
                        print ('of course! Taurus is an earth sign represented by the bull. Like')
                        print ('their celestial spirit animal, Taureans enjoy relaxing in serene,')
                        print ('bucolic environments surrounded by soft sounds, soothing aromas,')
                        print ('and succulent flavors.')
                        print ('====================================================================')
                if bval>31:
                        print ('EROR: Invalid date value for April.') 
        else:
            print ('')
            print ('ERROR: Input is not a number or input is not a valid date for April.')
    elif month=='May' or month=='MAY' or month=='may':
        print ('Note: Input only numerical values.')
        birthdate= input('Input your birthday:')
        try:
            bval= int(birthdate)
        except:
            bval= -1
        if bval>0:
            print ('')
            if bval >=1:
                if bval <=20:
                    print ('====================================================================')
                    print ('Your zodiac sign is:')
                    print ('                            Taurus')
                    print ('What sign is more likely to take a six-hour bath followed by a')
                    print ('luxurious Swedish massage and decadent dessert spread? Why Taurus,')
                    print ('of course! Taurus is an earth sign represented by the bull. Like')
                    print ('their celestial spirit animal, Taureans enjoy relaxing in serene,')
                    print ('bucolic environments surrounded by soft sounds, soothing aromas,')
                    print ('and succulent flavors.')
                    print ('====================================================================')
                if bval >=21:
                    if bval <=31:
                        print ('====================================================================')
                        print ('Your zodiac sign is:')
                        print ('                            Gemini')
                        print ('Have you ever been so busy that you wished you could clone yourself')
                        print ("to get everything done? That's the Gemini experience in a nutshell.")
                        print ('Spontaneous, playful, and adorably erratic, Gemini is driven by')
                        print ('insatiable curiosity. Appropriately symbolized by the celestial')
                        print ('twins, this air sign was interested in so many pursuits that it had')
                        print ('to double itself. You know, NBD!')
                        print ('====================================================================')
                if bval>31:
                        print ('EROR: Invalid date value for May.') 
        else:
            print ('')
            print ('ERROR: Input is not a number or input is not a valid date for May.')
    elif month=='June' or month=='JUNE' or month=='june':
        print ('Note: Input only numerical values.')
        birthdate= input('Input your birthday:')
        try:
            bval= int(birthdate)
        except:
            bval= -1
        if bval>0:
            print ('')
            if bval >=1:
                if bval <=20:
                    print ('====================================================================')
                    print ('Your zodiac sign is:')
                    print ('                            Gemini')
                    print ('Have you ever been so busy that you wished you could clone yourself')
                    print ("to get everything done? That's the Gemini experience in a nutshell.")
                    print ('Spontaneous, playful, and adorably erratic, Gemini is driven by')
                    print ('insatiable curiosity. Appropriately symbolized by the celestial')
                    print ('twins, this air sign was interested in so many pursuits that it had')
                    print ('to double itself. You know, NBD!')
                    print ('====================================================================')
                if bval >=21:
                    if bval <=31:
                        print ('====================================================================')
                        print ('Your zodiac sign is:')
                        print ('                            Cancer')
                        print ('Represented by the crab, Cancer seamlessly weaves between the sea')
                        print ('and shore representing Cancer’s ability to exist in both emotional')
                        print ('and material realms. Cancers are highly intuitive and their psychic')
                        print ('abilities manifest in tangible spaces. But just like the')
                        print ('hard-shelled crustacean, this water sign is willing to do whatever')
                        print ('it takes to protect itself emotionally. In order to get to know this')
                        print ("sign, you're going to need to establish trust")
                        print ('====================================================================')
                if bval>31:
                        print ('EROR: Invalid date value for June.') 
        else:
            print ('')
            print ('ERROR: Input is not a number or input is not a valid date for June.')
    elif month=='July' or month=='JULY' or month=='july':
        print ('Note: Input only numerical values.')
        birthdate= input('Input your birthday:')
        try:
            bval= int(birthdate)
        except:
            bval= -1
        if bval>0:
            print ('')
            if bval >=1:
                if bval <=22:
                    print ('====================================================================')
                    print ('Your zodiac sign is:')
                    print ('                            Cancer')
                    print ('Represented by the crab, Cancer seamlessly weaves between the sea')
                    print ('and shore representing Cancer’s ability to exist in both emotional')
                    print ('and material realms. Cancers are highly intuitive and their psychic')
                    print ('abilities manifest in tangible spaces. But just like the')
                    print ('hard-shelled crustacean, this water sign is willing to do whatever')
                    print ('it takes to protect itself emotionally. In order to get to know this')
                    print ("sign, you're going to need to establish trust")
                    print ('====================================================================')
                if bval >=23:
                    if bval <=31:
                        print ('====================================================================')
                        print ('Your zodiac sign is:')
                        print ('                            Leo')
                        print ('Roll out the red carpet because Leo has arrived! Passionate, loyal,')
                        print ('and infamously dramatic, Leo is represented by the lion and these')
                        print ('spirited fire signs are the kings and queens of the celestial')
                        print ("jungle. They're delighted to embrace their royal status: Vivacious,")
                        print ('theatrical, and fiery, Leos love to bask in the spotlight and')
                        print ('celebrate…well, themselves.')
                        print ('====================================================================')
                if bval>31:
                        print ('EROR: Invalid date value for July.') 
        else:
            print ('')
            print ('ERROR: Input is not a number or input is not a valid date for July.')
    elif month=='August' or month=='AUGUST' or month=='august':
        print ('Note: Input only numerical values.')
        birthdate= input('Input your birthday:')
        try:
            bval= int(birthdate)
        except:
            bval= -1
        if bval>0:
            print ('')
            if bval >=1:
                if bval <=22:
                    print ('====================================================================')
                    print ('Your zodiac sign is:')
                    print ('                            Leo')
                    print ('Roll out the red carpet because Leo has arrived! Passionate, loyal,')
                    print ('and infamously dramatic, Leo is represented by the lion and these')
                    print ('spirited fire signs are the kings and queens of the celestial')
                    print ("jungle. They're delighted to embrace their royal status: Vivacious,")
                    print ('theatrical, and fiery, Leos love to bask in the spotlight and')
                    print ('celebrate…well, themselves.')
                    print ('====================================================================')
                if bval >=23:
                    if bval <=31:
                        print ('====================================================================')
                        print ('Your zodiac sign is:')
                        print ('                            Virgo')
                        print ('You know the expression, "If you want something done, ask a busy')
                        print ('person?" Well, that definitely is the Virgo anthem. Virgos are')
                        print ('logical, practical, and systematic in their approach to life. Virgo')
                        print ('is an earth sign historically represented by the goddess of wheat')
                        ptint ("and agriculture, an association that speaks to Virgo's deep-rooted")
                        print ('presence in the material world. This earth sign is a perfectionist')
                        print ("at heart and isn’t afraid to improve skills through diligent and")
                        print ('consistent practice.')
                        print ('====================================================================')
                if bval>31:
                        print ('EROR: Invalid date value for August.') 
        else:
            print ('')
            print ('ERROR: Input is not a number or input is not a valid date for August.')
    elif month=='September' or month=='SEPTEMBER' or month=='september':
        print ('Note: Input only numerical values.')
        birthdate= input('Input your birthday:')
        try:
            bval= int(birthdate)
        except:
            bval= -1
        if bval>0:
            print ('')
            if bval >=1:
                if bval <=22:
                    print ('====================================================================')
                    print ('Your zodiac sign is:')
                    print ('                            Virgo')
                    print ('You know the expression, "If you want something done, ask a busy')
                    print ('person?" Well, that definitely is the Virgo anthem. Virgos are')
                    print ('logical, practical, and systematic in their approach to life. Virgo')
                    print ('is an earth sign historically represented by the goddess of wheat')
                    ptint ("and agriculture, an association that speaks to Virgo's deep-rooted")
                    print ('presence in the material world. This earth sign is a perfectionist')
                    print ("at heart and isn’t afraid to improve skills through diligent and")
                    print ('consistent practice.')
                    print ('====================================================================')
                if bval >=23:
                    if bval <=31:
                        print ('====================================================================')
                        print ('Your zodiac sign is:')
                        print ('                            Libra')
                        print ('Balance, harmony, and justice define Libra energy. As a cardinal air')
                        print ('sign, Libra is represented by the scales (interestingly, the only')
                        print ('inanimate object of the zodiac), an association that reflects')
                        print ("Libra's fixation on establishing equilibrium. Libra is obsessed with")
                        print ('symmetry and strives to create equilibrium in all areas of')
                        print ('life—especially when it comes to matters of the heart.')
                        print ('====================================================================')
                if bval>31:
                        print ('EROR: Invalid date value for September.') 
        else:
            print ('')
            print ('ERROR: Input is not a number or input is not a valid date for September.')
    elif month=='October' or month=='OCTOBER' or month=='october':
        print ('Note: Input only numerical values.')
        birthdate= input('Input your birthday:')
        try:
            bval= int(birthdate)
        except:
            bval= -1
        if bval>0:
            print ('')
            if bval >=1:
                if bval <=22:
                    print ('====================================================================')
                    print ('Your zodiac sign is:')
                    print ('                            Libra')
                    print ('Balance, harmony, and justice define Libra energy. As a cardinal air')
                    print ('sign, Libra is represented by the scales (interestingly, the only')
                    print ('inanimate object of the zodiac), an association that reflects')
                    print ("Libra's fixation on establishing equilibrium. Libra is obsessed with")
                    print ('symmetry and strives to create equilibrium in all areas of')
                    print ('life—especially when it comes to matters of the heart.')
                    print ('====================================================================')
                if bval >=23:
                    if bval <=31:
                        print ('====================================================================')
                        print ('Your zodiac sign is:')
                        print ('                            Scorpio')
                        print ('Elusive and mysterious, Scorpio is one of the most misunderstood')
                        print ('signs of the zodiac. Scorpio is a water sign that uses emotional')
                        print ('energy as fuel, cultivating powerful wisdom through both the')
                        print ('physical and unseen realms. In fact, Scorpio derives extraordinary')
                        print ('courage from its psychic abilities, which is what makes this sign')
                        print ('one of the most complicated and dynamic of the zodiac.')
                        print ('====================================================================')
                if bval>31:
                        print ('EROR: Invalid date value for October.') 
        else:
            print ('')
            print ('ERROR: Input is not a number or input is not a valid date for October.')
    elif month=='November' or month=='NOVEMBER' or month=='november':
        print ('Note: Input only numerical values.')
        birthdate= input('Input your birthday:')
        try:
            bval= int(birthdate)
        except:
            bval= -1
        if bval>0:
            print ('')
            if bval >=1:
                if bval <=21:
                    print ('====================================================================')
                    print ('Your zodiac sign is:')
                    print ('                            Scorpio')
                    print ('Elusive and mysterious, Scorpio is one of the most misunderstood')
                    print ('signs of the zodiac. Scorpio is a water sign that uses emotional')
                    print ('energy as fuel, cultivating powerful wisdom through both the')
                    print ('physical and unseen realms. In fact, Scorpio derives extraordinary')
                    print ('courage from its psychic abilities, which is what makes this sign')
                    print ('one of the most complicated and dynamic of the zodiac.')
                    print ('====================================================================')
                if bval >=22:
                    if bval <=31:
                        print ('====================================================================')
                        print ('Your zodiac sign is:')
                        print ('                            Sagittarius')
                        print ('Oh, the places Sagittarius goes! But…actually. This fire sign knows')
                        print ('no bounds. Represented by the archer, Sagittarians are always on a')
                        print ('quest for knowledge. The last fire sign of the zodiac, Sagittarius')
                        print ('launches its many pursuits like blazing arrows, chasing after')
                        print ('geographical, intellectual, and spiritual adventures.')
                        print ('====================================================================')
                if bval>31:
                        print ('EROR: Invalid date value for November.') 
        else:
            print ('')
            print ('ERROR: Input is not a number or input is not a valid date for November.')
    elif month=='December' or month=='DECEMBER' or month=='december':
        print ('Note: Input only numerical values.')
        birthdate= input('Input your birthday:')
        try:
            bval= int(birthdate)
        except:
            bval= -1
        if bval>0:
            print ('')
            if bval >=1:
                if bval <=21:
                    print ('====================================================================')
                    print ('Your zodiac sign is:')
                    print ('                            Sagittarius')
                    print ('Oh, the places Sagittarius goes! But…actually. This fire sign knows')
                    print ('no bounds. Represented by the archer, Sagittarians are always on a')
                    print ('quest for knowledge. The last fire sign of the zodiac, Sagittarius')
                    print ('launches its many pursuits like blazing arrows, chasing after')
                    print ('geographical, intellectual, and spiritual adventures.')
                    print ('====================================================================')
                if bval >=22:
                    if bval <=31:
                        print ('====================================================================')
                        print ('Your zodiac sign is:')
                        print ('                            Capricorn')
                        print ('What is the most valuable resource? For Capricorn, the answer is')
                        print ('clear: time. Capricorn is climbing the mountain straight to the top')
                        print ('and knows that patience, perseverance, and dedication are the only')
                        print ('way to scale. Capricorn, the last earth sign of the zodiac, is')
                        print ('represented by the sea goat, a mythological creature with the body')
                        print ('of a goat and the tail of a fish. Accordingly, Capricorns are')
                        print ('skilled at navigating both the material and emotional realms.')
                        print ('====================================================================')
                if bval>31:
                        print ('EROR: Invalid date value for December.') 
        else:
            print ('')
            print ('ERROR: Input is not a number or input is not a valid date for December.')
    #for instances where the month inputted is not in the list of months of a year, misspelled, or abbreviated;—
    #the error will be displayed
    else:
        print ('ERROR: Could not find a match. Please input a correct birth month.')               






