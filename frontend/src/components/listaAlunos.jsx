import React, { Component } from 'react';

class ListaAlunos extends Component {
    state = {
        data: [],
        loaded: false
    }

    componentDidMount() {
        fetch("http://localhost:8000/alunos/")
          .then(response => {
            if (response.status > 400) {
            // Código do comportamento em caso de problema na req
            }
            return response.json();
          })
          .then(data => {
            this.setState(() => {
              return {
                data,
                loaded: true
              };
            });
          });
      }
    
      render() {
        return (
            <div>
            {this.state.data.map(aluno => {
              return (
                <h2 key={aluno.id} className='App-table'>
                  {aluno.nome}
                </h2>
              );
            })}
          </div>
        );
      }
    }

export default ListaAlunos;