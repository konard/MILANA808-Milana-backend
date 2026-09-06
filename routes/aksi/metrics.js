const express = require('express');
const router = express.Router();

// GET /aksi/metrics
router.get('/', (req, res) => {
    res.json({ metrics: { uptime: process.uptime(), logsCount: 0 } });
});

module.exports = router;
