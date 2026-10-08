-- Rode uma vez no banco "biblioteca":  psql -U postgres -d biblioteca -f schema.sql

CREATE TABLE IF NOT EXISTS autor (
    id            SERIAL PRIMARY KEY,
    nome          VARCHAR(100) NOT NULL,
    nacionalidade VARCHAR(50)  NOT NULL
);

CREATE TABLE IF NOT EXISTS livro (
    id             SERIAL PRIMARY KEY,
    titulo         VARCHAR(150) NOT NULL,
    ano_publicacao INTEGER      NOT NULL,
    autor_id       INTEGER      NOT NULL
        REFERENCES autor(id) ON DELETE RESTRICT
    -- DECISAO DA DUPLA: RESTRICT bloqueia excluir autor que tem livros.
    -- Se preferirem apagar os livros junto, troque por ON DELETE CASCADE.
);
