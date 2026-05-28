import type {NextPage} from "next";
import styles from "../styles/Home.module.css"
import React, {useEffect, useState} from "react";
import Livro from "../classes/modelo/Livro";
import {Menu} from "../componentes/Menu";
import {LinhaLivro} from "../componentes/LinhaLivro";
import Head from "next/head";
import ControleLivros from "../classes/controle/ControleLivros";

const controleLivros = new ControleLivros();

const LivroLista: NextPage = () => {
    const [livros, setLivros] = useState<Array<Livro>>([])
    const [carregado, setCarregado] = useState(false);

    const excluir = (codigo: string) => {
        controleLivros.excluir(codigo).then(() => {
            setCarregado(false);
        });
    };

    useEffect(() => {
        if (!carregado) {
            controleLivros.obterLivros().then((resultado) => {
                setLivros(resultado);
                setCarregado(true);
            });
        }
    }, [carregado]);

    return (
        <div className={styles.conteiner}>
            <Head>
                <title>Catálogo de Livros</title>
                <meta name="viewport" content="width=device-width, initial-scale=1"/>
            </Head>
            <Menu/>
            <main className='container'>
                {!carregado && (<div className={styles.load}>
                    <div className={styles.load_box}>
                        <div className={styles.load_box_circle}></div>
                        <p className={styles.load_box_title}>Aguarde, carregando...</p>
                    </div>
                </div>)}
                <h1>Catálogo de Livros</h1>
                <table className="table table-striped">
                    <thead className="table-dark">
                    <tr>
                        <th scope="col">Título</th>
                        <th scope="col">Resumo</th>
                        <th scope="col">Editora</th>
                        <th scope="col">Autores</th>
                    </tr>
                    </thead>
                    <tbody>
                    {livros.map((livro, index) => (
                        <LinhaLivro key={index} livro={livro} excluir={excluir}/>
                    ))}
                    </tbody>
                </table>
            </main>
        </div>
    );
}

export default LivroLista;