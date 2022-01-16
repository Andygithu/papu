def main():
    #INDEX POSITION
    DATES = 0
    CREDITS = 1
    CLASSES = 2

    year = input('Enter the year and season to get your classes information(Ex:Winter 2022 ): ')
    degree_classes_dic = {
        'Winter 2022': ['Jan 5 - Apr 7','9 credits',['REL 250C - Jesus Christ Everlasting Gospel','CSE 121B - JavaScript Languaje','CSE 210 - Programming with classes','WDD 230 - Web Frontend Development I','GS 170- Career Development']],
        'Spring 2022': ['Apr 18 - Jul 20','8 credits',['REL 275 - Teachings of book of mormon','ENG 150 - Writing & Reasoning Foundations','WDD 330 - Web Frontend Development II']],
        'Fall 2022': ['Sep 12- Dec 14','8 credits',['REL 200C - The Eternal Family','MATH 108X - Math for the Real World','CSE 340 - Web Backend Development I']],
        'Winter 2023': ['Jan 4 - Apr 6','8 credits',['REL 225C - Foundations of the Restoration','BUS 301 - Adv Writing in Pro Contexts','CSE 341 - Web Backend Development II']],
        'Spring 2023': ['Apr 17 - Jul 19','9 credits',['HUM 110 - Introduction to the Humanities','CIT 111 - Introduction to Databases','WDD 430 - Web Full-Stack Development']],
        'Fall 2023': ['Sep 11 - Dec 13','8 credits',['REL 333 - Teachings of the Living Prophets','NUTR 150 - Essentials of Human Nutrition','CIT 225 - Databases Design & Development']],
        'Winter 2024': ['Jan 8 - Apr 10','8 credits',['REL 324 - Doctrina and Covenants','GESCI101 - From Atoms to Humans','CIT 325 - Databases Programming']],
        'Spring 2024': ['Apr 22 - Jul 24','8 credits',['FAM 160 - Family Relations','REL 325 - Doctrine and Covenants','CIT 326 - Database Administration']],
        'Fall 2024': ['Sep 16 - Dec 18','9 credits',['CIT 498 - Internship','ECON 150 - Econ Principles & Problems Micro','CIT 327 - Data Warehousing']],
        'Winter 2025' : ['Jan 6 - Apr 11','6 credits',['COMM 130 - Visual Media','BUS 115 - Business Applications']],
        'Spring 2025' : ['Apr 21 - Jul 25','9 credits',['CIT 240 - Networking','CIT 352 - Operating System I','COMM 175 - Communication Essentials']],
        'Fall 2025': ['Sep 15 - Dec 19','9 credits',['CIT 241 - Networking Design I','CIT 270 - System Security I','CIT 353 - Operating Systems II']],
        'Winter 2026': ['Jan 5 - Apr 10','6 credits',['CIT 381 - Business Intel and Analytics','CSE471 - Human-Computer Interaction']]
  
    }
    year.split('2')
    if year in degree_classes_dic:
        l = degree_classes_dic[year]
        dates = l[0]
        credits = l[1]
        classes = l[2]
        print()
        print(f'Start/End dates: {dates}')
        print(f'Numbers of credits to earn: {credits}')
        print()
        print('You are going to take these classes this semester:')
        print()
        for i in classes:
            print(i)
    else:
        print('Please type the correct year and season')
if __name__ == "__main__":      
    main()
