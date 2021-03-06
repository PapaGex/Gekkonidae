const router = require('express').Router();
let User = require('../models/User.model');

router.route('/user').get((req, res) => {
    User.find()
        .then(user => res.json(user))
        .catch(err => res.status(400).json('Error: ' + err));
});

router.route('/user').post((req, res) => {
    const username = req.body.username;
    const password = req.body.password;

    const user = new User({
        username,
        password,
    });

    newUser.save()
       .then(() => res.json('User Attached!'))
       .catch(err => res.status(400).json('Error: ' + err));
});

router.route('/:id').get((req, res) => {
    User.findById(req.params.id)
        .then(user => res.json(user))
        .catch(err => res.status(400).json('Error: ' + err));
});

router.route('/:id').delete((req, res) => {
    User.findByIdAndDelete(req.params.id)
        .then(() => res.json('User EXTERMINATED!'))
        .catch(err => res.status(400).json('Error: ' + err));
});

router.route('/update/:id').post((req, res) => {
    User.findById(req.params.id)
        .then(user => {
            user.username = req.body.username;
            user.password = req.body.password;

            user.save()
                .then(() => res.json('User Adapted!'))
                .catch(err => res.status(400).json('Error: ' + err));
               })
        .catch(err => res.status(400).json('Error: ' + err));
});

module.exports = router;