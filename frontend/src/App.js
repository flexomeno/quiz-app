import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [file, setFile] = useState(null);
  const [questions, setQuestions] = useState([]);
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [answers, setAnswers] = useState([]);
  const [score, setScore] = useState(null);

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleFileUpload = async () => {
    const formData = new FormData();
    formData.append('file', file);

    await axios.post('https://your-api-endpoint/upload', formData);
    fetchQuestions();
  };

  const fetchQuestions = async () => {
    const response = await axios.get('https://your-api-endpoint/questions');
    setQuestions(response.data);
  };

  const handleAnswerSubmit = (questionId, answerText) => {
    setAnswers([...answers, { questionId, text: answerText }]);
    setCurrentQuestion(currentQuestion + 1);
  };

  const handleSubmitQuiz = async () => {
    const response = await axios.post('https://your-api-endpoint/submit-answers', { answers });
    setScore(response.data.score);
  };

  return (
    <div>
      <h1>Quiz App</h1>
      {score !== null ? (
        <h2>Your Score: {score}</h2>
      ) : (
        <>
          {currentQuestion < questions.length ? (
            <div>
              <h2>{questions[currentQuestion].question}</h2>
              {questions[currentQuestion].answers.map((answer, index) => (
                <button key={index} onClick={() => handleAnswerSubmit(questions[currentQuestion].id, answer.text)}>
                  {answer.text}
                </button>
              ))}
            </div>
          ) : (
            <button onClick={handleSubmitQuiz}>Submit Quiz</button>
          )}
          <input type="file" onChange={handleFileChange} />
          <button onClick={handleFileUpload}>Upload Questions</button>
        </>
      )}
    </div>
  );
}

export default App;
