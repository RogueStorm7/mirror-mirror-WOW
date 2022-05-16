var myQuestions = [
	{
		question: "1. Did you feel that you didn't have enough to eat, had to wear dirty clothes, or had no one to protect you?",
		answers: {
			a: 'Yes',
			b: 'No'
		},
		correctAnswer: 'a'
	},
	{
		question: "2. Did you lose a parent through divorce, abandonment, death, or another reason?",
		answers: {
			a: 'Yes',
			b: 'No'
		},
		correctAnswer: 'a'
	},
    {
		question: "3. Did you live with anyone who was depressed, mentally ill, or attempted suicide?",
		answers: {
			a: 'Yes',
			b: 'No'
		},
		correctAnswer: 'a'
	},
    {
		question: "4. Did you live with anyone who had a problem with drinking or using drugs, including prescription drugs?",
		answers: {
            a: 'Yes',
			b: 'No'
		},
		correctAnswer: 'a'
	},
    {
		question: "5. Did your parents or adults in your home ever hit, punch, beat, or threaten to harm each other?",
		answers: {
			a: 'Yes',
			b: 'No'
		},
		correctAnswer: 'a'
	},
    {
		question: "6. Did you live with anyone who went to jail or prison?",
		answers: {
			a: 'Yes',
			b: 'No'
		},
		correctAnswer: 'a'
	},
    {
		question: "7. Did a parent or adult in your home ever swear at you, insult you, or put you down?",
		answers: {
			a: 'Yes',
			b: 'No'
		},
		correctAnswer: 'a'
	},
    {
		question: "8. Did a parent or adult in your home ever hit, beat, kick, or physically hurt you in any way?",
		answers: {
			a: 'Yes',
			b: 'No'
		},
		correctAnswer: 'a'
	},
    {
		question: "9. Did you feel that no one in your family loved you or thought you were special?",
		answers: {
			a: 'Yes',
			b: 'No'
		},
		correctAnswer: 'a'
	},
    {
		question: "10. Did you experience unwanted sexual contact- such as: fondling and/or oral/anal/vaginal penetration?",
		answers: {
            a: 'Yes',
			b: 'No'
		},
		correctAnswer: 'a'
	}
];

var quizContainer = document.getElementById('quiz');
var resultsContainer = document.getElementById('results');
var submitButton = document.getElementById('submit');

generateQuiz(myQuestions, quizContainer, resultsContainer, submitButton);

function generateQuiz(questions, quizContainer, resultsContainer, submitButton){

	function showQuestions(questions, quizContainer){
        // we'll need a place to store the output and the answer choices
        var output = [];
        var answers;
    
        // for each question...
        for(var i=0; i<questions.length; i++){
            
            // first reset the list of answers
            answers = [];
    
            // for each available answer to this question...
            for(letter in questions[i].answers){
    
                // ...add an html radio button
                answers.push(
                    '<label>'
                        + '<input type="radio" name="question'+i+'" value="'+letter+'">'
                        + questions[i].answers[letter]
                    + '</label>'
                );
            }
    
            // add this question and its answers to the output
            output.push(
                '<div class="question">' + questions[i].question + '</div>'
                + '<div class="answers">' + answers.join('') + '</div>'
            );
        }
    
        // finally combine our output list into one string of html and put it on the page
        quizContainer.innerHTML = output.join('');
    }

	function showResults(questions, quizContainer, resultsContainer){
	
        // gather answer containers from our quiz
        var answerContainers = quizContainer.querySelectorAll('.answers');
        
        // keep track of user's answers
        var userAnswer = '';
        var numCorrect = 0;
        
        // for each question...
        for(var i=0; i<questions.length; i++){
    
            // find selected answer
            userAnswer = (answerContainers[i].querySelector('input[name=question'+i+']:checked')||{}).value;
            
            // if answer is correct
            if(userAnswer===questions[i].correctAnswer){
                // add to the number of correct answers
                numCorrect++;
            }
            // if answer is wrong or blank
            else{
                numCorrect+0;
            }
        }
    
        // show number of correct answers out of total
        resultsContainer.innerHTML = numCorrect;
    }

	// show the questions
	showQuestions(questions, quizContainer);

	// when user clicks submit, show results
    submitButton.onclick = function(){
        showResults(questions, quizContainer, resultsContainer);
    }
}