const express = require('express');
const router = express.Router();

let logs = [];

// GET /aksi/logs
router.get('/', (req, res) => {
    res.json({ logs });
});

// POST /aksi/logs/append
router.post('/append', (req, res) => {
    logs.push(req.body);
    res.json({ success: true });
});

// GET /aksi/logs/export
router.get('/export', (req, res) => {
    res.json({ export: logs });
});

module.exports = router;
