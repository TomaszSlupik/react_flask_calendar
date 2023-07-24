import './App.scss';
import {useState, useEffect} from 'react'
import axios from 'axios'

function App() {


  const [test, setTest] = useState([])

  useEffect(() => {
    axios.get('http://127.0.0.1:5000/api/dane_zawodow')
      .then(res => {
        setTest(JSON.parse(res.data))
        console.log(test)
        
      })
      .catch(err => {
        console.log(err)
      })
  }, [])

  console.log(test)

  return (
    <div className="App">
     <h1>Lista Zawodów</h1>
      <table>
        <thead>
          <tr>
            <th>Data</th>
            <th>Nazwa</th>
            <th>Miejsce</th>
          </tr>
        </thead>
        <tbody>
          {test.map((competition, index) => (
            <tr key={index}>
              <td>{competition.Data}</td>
              <td>{competition.Nazwa}</td>
              <td>{competition.Miejsce}</td>
            </tr>
          ))}
        </tbody>
      </table>

    </div>
  );
}

export default App;
