
import './App.css';
import ListaCursos from './components/listaCursos';
import Footer from './components/footer';
function App() {
  
  return (
    <div className="App">
      <header className="App-header">
        <a href='' className='headercursos' to={""}>Cursos</a>
        <a href='' className='headeralunos' to = {""}>Aluno</a>
      </header>
      <ListaCursos/>
      <Footer/>
    </div>
  );
}

export default App;
