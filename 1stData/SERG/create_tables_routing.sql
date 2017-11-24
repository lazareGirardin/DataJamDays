--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = off;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET escape_string_warning = off;

--
-- Name: routing; Type: SCHEMA; Schema: -; Owner: -
--

CREATE SCHEMA routing;


SET search_path = routing, pg_catalog;

SET default_with_oids = true;

--
-- Name: edges; Type: TABLE; Schema: routing; Owner: -
--

CREATE TABLE edges (
    edge_id integer NOT NULL,
    vertex_id1 integer,
    vertex_id2 integer,
    level1 integer,
    level2 integer,
    type character varying(20),
    door character varying(20),
    door_rev character varying(20),
    network character varying(20),
    length double precision,
    x1 double precision,
    y1 double precision,
    x2 double precision,
    y2 double precision,
    the_geom public.geometry,
    CONSTRAINT enforce_dims_the_geom CHECK ((public.ndims(the_geom) = 2)),
    CONSTRAINT enforce_geotype_the_geom CHECK (((public.geometrytype(the_geom) = 'LINESTRING'::text) OR (the_geom IS NULL))),
    CONSTRAINT enforce_srid_the_geom CHECK ((public.srid(the_geom) = 900913))
);


--
-- Name: vertices; Type: TABLE; Schema: routing; Owner: -
--

CREATE TABLE vertices (
    vertex_id integer NOT NULL,
    level integer,
    the_geom public.geometry,
    CONSTRAINT enforce_dims_the_geom CHECK ((public.ndims(the_geom) = 2)),
    CONSTRAINT enforce_geotype_the_geom CHECK (((public.geometrytype(the_geom) = 'POINT'::text) OR (the_geom IS NULL))),
    CONSTRAINT enforce_srid_the_geom CHECK ((public.srid(the_geom) = 900913))
);


--
-- Name: edges_pkey; Type: CONSTRAINT; Schema: routing; Owner: -
--

ALTER TABLE ONLY edges
    ADD CONSTRAINT edges_pkey PRIMARY KEY (edge_id);


--
-- Name: vertices_pkey; Type: CONSTRAINT; Schema: routing; Owner: -
--

ALTER TABLE ONLY vertices
    ADD CONSTRAINT vertices_pkey PRIMARY KEY (vertex_id);


--
-- Name: edges_the_geom_1335166950969; Type: INDEX; Schema: routing; Owner: -
--

CREATE INDEX edges_the_geom_1335166950969 ON edges USING gist (the_geom);


--
-- Name: edges_vertex_id1_1335166950797; Type: INDEX; Schema: routing; Owner: -
--

CREATE INDEX edges_vertex_id1_1335166950797 ON edges USING btree (vertex_id1);


--
-- Name: edges_vertex_id2_1335166950907; Type: INDEX; Schema: routing; Owner: -
--

CREATE INDEX edges_vertex_id2_1335166950907 ON edges USING btree (vertex_id2);


--
-- Name: vertices_the_geom_1335166951469; Type: INDEX; Schema: routing; Owner: -
--

CREATE INDEX vertices_the_geom_1335166951469 ON vertices USING gist (the_geom);


--
-- PostgreSQL database dump complete
--

