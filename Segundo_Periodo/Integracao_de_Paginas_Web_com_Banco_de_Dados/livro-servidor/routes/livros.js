const express = require('express');
const router = express.Router();
const { obterLivros, incluir, excluir } = require('../modelo/livro-dao');

// Rota GET para obter todos os livros
router.get('/', async (req, res) => {
  try {
    const livros = await obterLivros();
    res.json(livros);
  } catch (err) {
    res.status(500).json({ ok: false, mensagem: "Falha ao obter livros", erro: err.message });
  }
});

// Rota POST para incluir um novo livro
router.post('/', async (req, res) => {
  try {
    const livro = req.body;
    await incluir(livro);
    res.json({ ok: true, mensagem: "Livro incluído com sucesso!" });
  } catch (err) {
    res.status(500).json({ ok: false, mensagem: "Falha ao incluir livro: " + err.message });
  }
});

// Rota DELETE para excluir um livro pelo código (_id)
router.delete('/:id', async (req, res) => {
  try {
    const codigo = req.params.id;
    const resultado = await excluir(codigo);
    if (resultado.deletedCount > 0) {
      res.json({ ok: true, mensagem: "Livro excluído com sucesso!" });
    } else {
      res.status(404).json({ ok: false, mensagem: "Livro não encontrado para exclusão." });
    }
  } catch (err) {
    res.status(500).json({ ok: false, mensagem: "Falha ao excluir livro: " + err.message });
  }
});

module.exports = router;
