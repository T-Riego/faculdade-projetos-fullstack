const banco = require('./conexao');

const LivroSchema = new banco.Schema({
  _id: banco.Schema.Types.ObjectId,
  titulo: { type: String, required: true },
  codEditora: { type: Number, required: true },
  resumo: String,
  autores: [String]
});

const Livro = banco.model('Livro', LivroSchema, 'livros');

module.exports = Livro;
