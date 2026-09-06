const express = require('express');
const router = express.Router();

// GET /aksi/proof
router.get('/', (req, res) => {
    // Заглушка — здесь позже можно подключить AKSI-Core
    res.json({ proof: 'placeholder' });
});

module.exports = router;
