import {Component, OnInit} from '@angular/core';
import {Editora} from "../editora";
import {Livro} from "../livro";
import {ControleEditoraService} from "../controle-editora.service";
import {ControleLivrosService} from "../controle-livros.service";

@Component({
  selector: 'app-livro-lista',
  templateUrl: './livro-lista.component.html',
  styleUrls: ['./livro-lista.component.css']
})
export class LivroListaComponent implements OnInit {
  public editoras: Array<Editora> = [];
  public livros: Array<Livro> = [];

  servEditora: ControleEditoraService;
  servLivros: ControleLivrosService;

  constructor(servEditora: ControleEditoraService, servLivros: ControleLivrosService) {
    this.servEditora = servEditora;
    this.servLivros = servLivros;
  }

  ngOnInit(): void {
    this.editoras = this.servEditora.getEditoras();
    this.servLivros.obterLivros().then((resultado) => {
      this.livros = resultado;
    });
  }

  excluir = (codigo: string) => {
    this.servLivros.excluir(codigo).then(() => {
      this.servLivros.obterLivros().then((resultado) => {
        this.livros = resultado;
      });
    });
  }

  obterNome = (codEditora: number) => {
    return this.servEditora.getNomeEditora(codEditora);
  }
}
