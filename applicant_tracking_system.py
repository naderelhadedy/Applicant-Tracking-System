# decide_next_process function represents an applicant tracking system that takes your cv as an input and compare it with the wanted requirements and decide whether or not you pass to next step
def decide_next_process():
  """this function represents an applicant tracking system that takes your cv as an input and then
     compare it with the wanted requirements and decide whether or not you pass to next step"""
    # a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just", \
    "in", "on", "for"]
    # wanted requirements
    requirements = ["cpp", "python", "tensorflow", "tableau", "master", "bachelor"]
    
    # prompt user to input cv
    file_contents = input("Enter applicant's cv: \n")
    file_contents = file_contents.split()
    # store applicant's name
    applicant_name = "{} {}".format(file_contents[0], file_contents[1])
    # a list to store matching words
    words = []
    
    # loop through the input till the end
    i = 0
    while(i < len(file_contents)):
        if not file_contents[i].isalpha():
          # clean the input
          for symbol in punctuations:
            file_contents[i] = file_contents[i].replace(symbol, '')
            file_contents[i] = file_contents[i].replace("'s", '')
            
        if file_contents[i].lower() not in uninteresting_words:
          # store matching words
          if file_contents[i].lower() not in words and file_contents[i].lower() in requirements:
            words.append(file_contents[i].lower())
            
        i += 1
        
    # calculate the percentage of matching requirements to be compaerd with decided percentage which is 60%
    percentage = round(len(words)/len(requirements)*100)
    if percentage >= 60:
      result = "Pass To Next Step"
    else:
      result = "Didn't Pass Current Step"

    # format the output; name, matching requirements and final result
    print("\n\033[1;34mApplicant:\033[0m {}".format(applicant_name))
    print("\033[1;31mMatching Requirements:\033[0m")
    for word in words:
      print("{}".format(word.upper().center(25)))
    print("\033[1;35mStatus:\033[0m {}".format(result))
    

# call the function
decide_next_process()

# You can use this as an input
"""
Nader Elhadedy 
Skills:
     Cpp
     Python
     Java
     Tensorflow
     Tableau
      Go
Education:
    Bachelor's degree
    Master's degree
"""
"""
Nader Elhadedy Skills: Cpp Python Go TensorFlow Tableau Java Bachelor's Degree Master's Degree
"""