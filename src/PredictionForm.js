import { useState } from 'react';
import './prediction.css';

function PredictionForm() {
  const [title, setTitle] = useState('');
  const [genre, setGenre] = useState('');
  const [description, setDescription] = useState('');
  const [type, setType] = useState('');
  const [producer, setProducer] = useState('');
  const [studio, setStudio] = useState('');
  const [result, setResult] = useState(null);
  const [isNewPrediction, setIsNewPrediction] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();

    const response = await fetch("http://127.0.0.1:8000/", {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ title, genre, description, type, producer, studio })
    });

    const data = await response.json();
    setResult(data.prediction);
    setIsNewPrediction(true);
  }

  const handleNewPrediction = () => {
    setTitle('');
    setGenre('');
    setDescription('');
    setType('');
    setProducer('');
    setStudio('');
    setResult(null);
    setIsNewPrediction(false);
  }

  return (
    <form onSubmit={handleSubmit} >
      <label htmlFor="title">Anime Title :</label>
      <input type="text" id="title" value={title} onChange={(e) => setTitle(e.target.value)} required />

      <label htmlFor="genre">Anime Genre :</label>
      <input type="text" id="genre" value={genre} onChange={(e) => setGenre(e.target.value)} required />

      <label htmlFor="description">Anime Description :</label>
      <input type="text" id="description" value={description} onChange={(e) => setDescription(e.target.value)} required />

      <label htmlFor="type">Anime Type :</label>
      <input type="text" id="type" value={type} onChange={(e) => setType(e.target.value)} required />

      <label htmlFor="producer">Anime Producer :</label>
      <input type="text" id="producer" value={producer} onChange={(e) => setProducer(e.target.value)} required />

      <label htmlFor="studio">Anime Studio :</label>
      <input type="text" id="studio" value={studio} onChange={(e) => setStudio(e.target.value)} required />

      {isNewPrediction ?
        <button type="button" onClick={handleNewPrediction}>Effectuer une nouvelle prédiction</button>
        :
        <button type="submit">Faire une prédiction</button>
      }

      {result && <div className="result">{result}</div>}
    </form>
  );
}

export default PredictionForm;
