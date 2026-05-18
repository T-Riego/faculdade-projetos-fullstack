import { Injectable } from '@angular/core';
import { Livro } from './livro';

@Injectable({
  providedIn: 'root'
})
export class ControleLivrosService {
  private livros: Array<Livro> = [
    { codigo: 1, codEditora: 1, titulo: 'Código Limpo', resumo: 'Um guia clássico.', autores: ['Robert C. Martin'] },
    { codigo: 2, codEditora: 2, titulo: 'Engenharia de Software Moderna', resumo: 'Práticas.', autores: ['Valdemar Setzer'] },
    { codigo: 3, codEditora: 3, titulo: 'Padrões de Projeto', resumo: 'Soluções.', autores: ['Erich Gamma'] }
  ];

  constructor() { }

  obterLivros(): Array<Livro> {
    return this.livros;
  }

  incluir(livro: Livro): void {
    const codigoMaisAlto = this.livros.length > 0 
      ? Math.max(...this.livros.map(l => l.codigo)) 
      : 0;
      
    livro.codigo = codigoMaisAlto + 1;
    this.livros.push(livro);
  }

  excluir(codigo: number): void {
    const indice = this.livros.findIndex(livro => livro.codigo === codigo);
    if (indice !== -1) {
      this.livros.splice(indice, 1);
    }
  }
}
