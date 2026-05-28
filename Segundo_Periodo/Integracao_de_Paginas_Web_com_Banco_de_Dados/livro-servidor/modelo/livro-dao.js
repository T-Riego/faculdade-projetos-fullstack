const Livro = require('./livro-schema');

// Função obterLivros: Arrow Function, assíncrona, retorna o conjunto de livros obtidos com find
const obterLivros = async () => {
  try {
    return await Livro.find();
  } catch (err) {
    console.error("Erro ao obter livros:", err);
    throw err;
  }
};

// Função incluir: Arrow Function, assíncrona, recebe um livro JSON e invoca o método create
const incluir = async (livro) => {
  try {
    // Se o _id vier vazio ou nulo (como de formulários), removemos para que o MongoDB gere automaticamente
    if (!livro._id) {
      delete livro._id;
    }
    return await Livro.create(livro);
  } catch (err) {
    console.error("Erro ao incluir livro:", err);
    throw err;
  }
};

// Função excluir: Arrow Function, assíncrona, recebe um código (id) e invoca deleteOne usando o _id
const excluir = async (codigo) => {
  try {
    return await Livro.deleteOne({ _id: codigo });
  } catch (err) {
    console.error("Erro ao excluir livro:", err);
    throw err;
  }
};

module.exports = { obterLivros, incluir, excluir };
