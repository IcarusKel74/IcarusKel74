party_goers={'Andrew','Barb','Carole','David'}
print(party_goers)
print('partygoesr',type(party_goers))

attendee = input("Who are you looking for: ")

print("\nDid",attendee,"go to the party:\n",attendee in party_goers)

students={'John','David','Billy'}

extra_students=input("\nWho is the new student")
students.add(extra_students)

commons = party_goers.intersection(students)

party_students=list(commons)

print("\nWas the student called",attendee,"at the party:\n",attendee in party_students)