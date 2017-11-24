drop table public.locaux;
create table public.locaux
(
    gid serial not null,
    etage integer,
    room_abr character varying,
    room_din character varying,
    vertex_id integer,
    constraint locaux_pkey primary key (gid)
)
with (oids = false);
select addgeometrycolumn('public', 'locaux','the_geom', 900913, 'MULTIPOLYGON', 2);
