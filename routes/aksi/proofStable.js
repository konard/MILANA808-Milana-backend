const express = require('express');
const router = express.Router();

// POST /aksi/proof/stable
router.post('/', (req, res) => {
    // Сохраняем стабильный результат (пример)
    res.json({ success: true, saved: req.body });
});

module.exports = router;
