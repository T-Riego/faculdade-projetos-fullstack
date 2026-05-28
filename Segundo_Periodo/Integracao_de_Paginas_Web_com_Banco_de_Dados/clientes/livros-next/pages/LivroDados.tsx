import type {NextPage} from "next";
import React, {useState} from "react";
import ControleEditora from "../classes/controle/ControleEditora";
import Router from "next/router";
import {Menu} from "../componentes/Menu";
import ControleLivros from "../classes/controle/ControleLivros";
import Livro from "../classes/modelo/Livro";

const controleEditora = new ControleEditora();
const controleLivros = new ControleLivros();

const LivroDados: NextPage = () => {
    // Método que pega o array de editora e modifica colocando value e text
    const opcoes = controleEditora.getEditoras().map((editora) => ({
        value: editora.codEditora,
        text: editora.nome
    }));

    // Define as States iniciais
    const [titulo, setTitulo] = useState('');
    const [resumo, setResumo] = useState('');
    const [autores, setAutores] = useState('');
    const [codEditora, setCodEditora] = useState(opcoes.length > 0 ? opcoes[0].value : 0);

    const tratarCombo = (evento: any) => {
        const numerointeiro = parseInt(evento.target.value)
        setCodEditora(numerointeiro)
    }

    const incluir = (evento: any) => {
        evento.preventDefault();
        const autoresArray = autores.split("\n").map(autor => autor.trim());
        const livro = new Livro("", codEditora, titulo, resumo, autoresArray);

        controleLivros.incluir(livro).then(() => {
            Router.push("/LivroLista");
        });
    };

    return (
        <>
            <Menu/>
            <main className='container'>
                <h1>Dados do Livro</h1>
                <form onSubmit={incluir} method='post'>
                    <div className="form-group mb-3">
                        <label htmlFor="titulo">Título</label>
                        <input
                            type="text"
                            className="form-control"
                            id="titulo"
                            name='titulo'
                            value={titulo}
                            onChange={(evento) => setTitulo(evento.target.value)}
                            required
                        />
                    </div>

                    <div className="form-group mb-3">
                        <label htmlFor="resumo">Resumo</label>
                        <textarea
                            className="form-control"
                            id="resumo"
                            name='resumo'
                            value={resumo}
                            onChange={(evento) => setResumo(evento.target.value)}
                            required
                        ></textarea>
                    </div>

                    <div className="form-group mb-3">
                        <label htmlFor="editora">Editora</label>
                        <select 
                            className="form-control" 
                            id="editora" 
                            name='editora'
                            value={codEditora}
                            onChange={(evento) => tratarCombo(evento)}
                        >
                            {opcoes.map((opcao) => (
                                <option key={opcao.value} value={opcao.value}>{opcao.text}</option>
                            ))}
                        </select>
                    </div>

                    <div className="form-group mb-3">
                        <label htmlFor="autores">Autores (um por linha)</label>
                        <textarea
                            className="form-control"
                            id="autores"
                            name='autores'
                            value={autores}
                            onChange={(evento) => setAutores(evento.target.value)}
                            required
                        ></textarea>
                    </div>

                    <button type="submit" className="btn btn-primary">Salvar Dados</button>
                </form>
            </main>
        </>
    )
}

export default LivroDados;