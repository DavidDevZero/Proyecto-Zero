# Modelo de Datos: Proyecto Zero

## Usuario
- `id`: INTEGER, PRIMARY KEY, AUTOINCREMENT
- `email`: TEXT, UNIQUE, NOT NULL
- `password_hash`: TEXT, NOT NULL
- `fecha_registro`: TIMESTAMP, DEFAULT CURRENT_TIMESTAMP

## Ingreso
- `id`: INTEGER, PRIMARY KEY, AUTOINCREMENT
- `usuario_id`: INTEGER, FOREIGN KEY (usuarios.id)
- `cantidad`: REAL, NOT NULL
- `fuente`: TEXT
- `fecha`: TIMESTAMP, DEFAULT CURRENT_TIMESTAMP

## Gasto
- `id`: INTEGER, PRIMARY KEY, AUTOINCREMENT
- `usuario_id`: INTEGER, FOREIGN KEY (usuarios.id)
- `cantidad`: REAL, NOT NULL
- `categoria`: TEXT, NOT NULL
- `descripcion`: TEXT
- `fecha`: TIMESTAMP, DEFAULT CURRENT_TIMESTAMP