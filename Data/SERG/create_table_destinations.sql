drop table public.destinations;
create table public.destinations
(
    id serial not null,
    etage integer,
    theme character varying,
    nom character varying,
    vertex_id integer,
    constraint destinations_pkey primary key (id)
)
with (oids = false);
select addgeometrycolumn('public', 'destinations','the_geom', 900913, 'POINT', 2);
