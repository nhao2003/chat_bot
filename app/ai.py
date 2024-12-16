from prompt import prompt_template
import google.generativeai as genai

model = genai.GenerativeModel('gemini-1.5-flash', safety_settings={
genai.types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: genai.types.HarmBlockThreshold.BLOCK_NONE,
genai.types.HarmCategory.HARM_CATEGORY_HARASSMENT: genai.types.HarmBlockThreshold.BLOCK_NONE,
genai.types.HarmCategory.HARM_CATEGORY_HATE_SPEECH: genai.types.HarmBlockThreshold.BLOCK_NONE,
genai.types.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: genai.types.HarmBlockThreshold.BLOCK_NONE,
})

# result = model.generate_content("You are an AI-powered assistant supporting users on an online bookstore platform. Your task is to help users find relevant books based on their queries. When a user enters a query, you should search for relevant books in the database and provide a response based on the search results. If the user query matches a book title or description, you should return the book details. If the query does not match any book, you should provide a response indicating that no relevant books were found. You should also handle cases where the user query is empty or invalid. Your response should be informative and user-friendly, helping users find the information they need. You can use the search results to generate a response that best matches the user query. Remember to provide accurate and relevant information to enhance the user experience. /n/n User Query: What is the best erotica book to read and why? /n/n Search Results: Title: The Man I Love (The Fish Tales, #1), Description: \"Like it or not, she made you the man you are. And you never got over her. You just left.\"\nApril 19, 1992: A man with a gun walks into a university theater, intent on stopping the show. Erik \"Fish\" Fiskare watches from the lighting booth as his life is instantly and irrevocably changed.\nSpanning fifteen years, The Man I Loveexplores how a single act of violence reverberates through a circle of college friends. At the circle's center is Erik and his girlfriend, Marguerite \"Daisy\" Bianco. Her love, passion and pragmatic strength have always sustained Erik, but when she succumbs to post-traumatic stress, the young couple is torn apart.\nErik remains estranged from Daisy into his adulthood. He builds a satisfying life, yet he's haunted by the lingering bond of his soul mate. Soon Erik must face the past and answer the question: is leaving the end of loving?\nFearlessly touching on today's social and mental health issues, The Man I Lovefollows Erik's journey back to the truth of himself and a woman he can't forget. With its gripping story and an unforgettable cast of characters, this epic novel of love and forgiveness lingers long after the last page is turned.\n\"Laqueur's prose is solid and vivid.\"\n--Kirkus Reviews\n\"As intense, angsty, tumultuous and heartbreaking as a beautiful epic love story gets. Absolutely addicting. Laqueur is one of the most eloquent authors I have ever read.\"\n--Maryse\'s Book Blog\n\"Absolutely breathtaking... With its unique plotline and utterly exquisite writing, this is the kind of story you feel deep in your heart and that'll stay with you long after you finish reading.\"\n--Aestas Book Blog\n\"Astounding. This is the book you read when you want to jump heads and live another life or when you want to submerge yourself into another reality, blood, guts and all.\"\n--Emma Scott, author of RUSH\n\"This writer has the remarkable ability to shake each scene til it bleeds... This is one of those stories that will stay with you long after you finish the last page.\"\n--Mary Frame, author of Imperfect Chemistryand Imperfectly Criminal\n\"An affirmation of the transformative power of love, a conduit to getting lost in an intricate landscape of intimacy, and a masterfully crafted reminder that life is not a dress rehearsal.\"\n--Underground Book Reviews\n\"Five stars. The Man I Loveby Suanne Laqueur joins the handful of truly spectacular books I've read this year. The writing is gorgeous, each passage has a sort of rhythm that flows beautifully, drawing you deeper and deeper into Daisy and Erik's story.\"\n--Readers' Favorite Book Awards (gold medal, Realistic Fiction)Title: You Can Love Again: The Guide to Finding Love That Lasts in Later Life, Description: How Finding Love Changes\nOnce upon a time you were young and single and love was easy to find, and relatively\nuncomplicated. Life was like a blank canvas waiting for you to make your mark on it.\nThey were heady young days, filled with dreams and optimism. Back then you didn't know\nwhat you didn't know about love and relationships.\nAs the years passed you accumulated things, people, responsibilities and emotional\nbaggage. Life and love started to get complicated.\nThis book is for women who have been badly burnt by relationships. Very often it is much\nsafer to stay home with a good book, the cat and a glass of wine than taking the risk of trying\nto find love again.\nBelieve it or not, there are good men out there looking for love. Finding them may\nnecessitate kissing a few frogs, but the result is worth it.\nThere is lasting love out there waiting for you if you are willing to do the inner work\nnecessary to attract love to you.\nThis book will show you how to release the thoughts that may have served to protect you in\nthe past, but now hold you back from the true love you deserve.\nYou will learn what you need to be happy in a relationship and what type of relationship suits\nyour current life stage.\nI can promise you that this book will change the way you think about relationships including\nyour relationship with yourself. Title: Mr. & Mrs. Fitzwilliam Darcy: Two Shall Become One (Darcy Saga #1), Description: A honeymoon can last a lifetime\n\"A book that addresses all the unanswered questions...\"\nBeginning on their wedding day, Darcy and Elizabeth are two people who are deeply in love with one another and are excited to begin their marriage.\nTheir courtship was tempestuous; misunderstandings and misgivings nearly tore them apart. But now that they've seen each other without prejudice, their trust, attraction, and delight in each other grows with every passing day. Both are inexperienced and innocent, sharing moments of shyness and boldness as they discover the kinds of intimacies that a newlywed couple shares.\nAs their love story unfolds, they reveal their innermost secrets and feelings, embracing each other in a marriage filled with romance, passion, humor, and drama that will keep you spellbound. Title: CareGifters Book Series Love: A Collection of Essays by Those Who Care, Description: Love, our fifth book in our CareGifters Book Series, features the poems, essays and artwork of family caregivers who turn love into a coping strategy. These family caregivers write of their love, remembering how they fell in love years before caregiving arrived and reflecting on how they stay in love long after caregiving stays.\nOur book features love from all perspectives--between siblings, parents and children, spouses. A granddaughter becomes the memory keeper for a grandmother she loves dearly. A grandmother finds a hero in a little boy who she treasures.\n\"When hubby had his accident it never dawned on me to love him less,\" Laura George writes. Which reminds me us that life's tough times will test our love. When tested, we can remember we choose how to use our love. In a time that seems to test our limits, we can love without limits.")

def generate_response(query, source_information):
    # Generate response using the prompt chain
    response = model.generate_content(prompt_template.format(query=query, source_information=source_information))
    return response.text