db.createUser(
    {
        user: 'root-master',
        pwd: 'password-master',
        roles: [
            {
                role: 'readWrite',
                db: 'db-fzsports'
            }
        ]
    }
)