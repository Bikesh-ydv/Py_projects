# quiz
questions = ("1. What is the capital city of Nepal?",
             "2. Which mountain is the highest peak in Nepal and the world?",
             "3. What is the national flower of Nepal?",
             "4. Who is considered the founder of modern Nepal?",
             "5. Which religion originated in Nepal?")
options = (("A.Pokhara","B.Lalitpur","C.Kathmandu","D.Bhaktapur"),
           ("A.Mount Annapurna","B.Mount Dhaulagiri","C.Mount Kanchenjunga","D.Mount Everest"),
           ("A.Rhododendron","B.Sunflower","C.Rose","D.Lotus"),
           ("A.Prithvi Narayan Shah","B.King Mahendra","C.Tribhuvan Bir Bikram Shah","D.Jung Bahadur Rana"),
           ("A.Hinduism","B.Islam","C.Buddhism","D.Christianity"))
answers = ("C","D","A","A","C");
guesses = [];
score =0;
question_num = 0;

for question in questions :
    print("------------------");
    print(question); 
    for option in options[question_num]:
     print(option);
     
    guess = input("Enter (A,B,C,D):").upper();
    guesses.append(guess);
    if guess == answers[question_num] :
       print("Correct!!!");
       score +=1;
    else:
       print("InCorrect!!!"); 
    question_num += 1;

print("----------------");
print(    "Result"      );
print("----------------");

print("answer:")
for answer in answers :
   
   print(answer,end = " ");
print();
print("Guess:")
for guess in guesses :
   print(guess,end = " ");
print();
score = (score/question_num)*100;
print(f"Your final score :{score}%");
