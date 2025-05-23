PGDMP      1                }            LocalPro    17.4    17.4     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                           false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                           false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                           false            �           1262    25082    LocalPro    DATABASE     p   CREATE DATABASE "LocalPro" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'es-CL';
    DROP DATABASE "LocalPro";
                     postgres    false            �            1259    25103    CONTRATO    TABLE       CREATE TABLE public."CONTRATO" (
    id_contrato integer NOT NULL,
    rut_usuario character varying(20),
    id_servicio integer,
    id_profesional integer,
    "Fecha" character varying(20),
    "Estado" character varying(20),
    "Descripcion" character varying(300)
);
    DROP TABLE public."CONTRATO";
       public         heap r       postgres    false            �            1259    25088    PROFESIONAL    TABLE     �   CREATE TABLE public."PROFESIONAL" (
    id_profesional integer NOT NULL,
    rut_usuario character varying(20),
    "Oficio" character varying(50),
    "Verificacion" character varying(200),
    "Valoracion" character varying(50)
);
 !   DROP TABLE public."PROFESIONAL";
       public         heap r       postgres    false            �            1259    25123    RESEÑA    TABLE     �   CREATE TABLE public."RESEÑA" (
    rut_usuario character varying(20),
    id_profesional integer,
    "Comentario" character varying(200),
    "Calificacion" integer
);
    DROP TABLE public."RESEÑA";
       public         heap r       postgres    false            �            1259    25098    SERVICIO    TABLE     �   CREATE TABLE public."SERVICIO" (
    id_servicio integer NOT NULL,
    tipo_servicio character varying(100),
    "Descripcion" character varying(300),
    precio_base bigint
);
    DROP TABLE public."SERVICIO";
       public         heap r       postgres    false            �            1259    25083    USUARIO    TABLE     �   CREATE TABLE public."USUARIO" (
    rut_usuario character varying(20) NOT NULL,
    "Nombre" character varying(50),
    "Email" character varying(50),
    tipo_usuario character varying(20)
);
    DROP TABLE public."USUARIO";
       public         heap r       postgres    false            �          0    25103    CONTRATO 
   TABLE DATA           }   COPY public."CONTRATO" (id_contrato, rut_usuario, id_servicio, id_profesional, "Fecha", "Estado", "Descripcion") FROM stdin;
    public               postgres    false    220   �       �          0    25088    PROFESIONAL 
   TABLE DATA           l   COPY public."PROFESIONAL" (id_profesional, rut_usuario, "Oficio", "Verificacion", "Valoracion") FROM stdin;
    public               postgres    false    218   �       �          0    25123    RESEÑA 
   TABLE DATA           ^   COPY public."RESEÑA" (rut_usuario, id_profesional, "Comentario", "Calificacion") FROM stdin;
    public               postgres    false    221   �       �          0    25098    SERVICIO 
   TABLE DATA           \   COPY public."SERVICIO" (id_servicio, tipo_servicio, "Descripcion", precio_base) FROM stdin;
    public               postgres    false    219          �          0    25083    USUARIO 
   TABLE DATA           Q   COPY public."USUARIO" (rut_usuario, "Nombre", "Email", tipo_usuario) FROM stdin;
    public               postgres    false    217   9       7           2606    25107    CONTRATO CONTRATO_pkey 
   CONSTRAINT     a   ALTER TABLE ONLY public."CONTRATO"
    ADD CONSTRAINT "CONTRATO_pkey" PRIMARY KEY (id_contrato);
 D   ALTER TABLE ONLY public."CONTRATO" DROP CONSTRAINT "CONTRATO_pkey";
       public                 postgres    false    220            3           2606    25092    PROFESIONAL PROFESIONAL_pkey 
   CONSTRAINT     j   ALTER TABLE ONLY public."PROFESIONAL"
    ADD CONSTRAINT "PROFESIONAL_pkey" PRIMARY KEY (id_profesional);
 J   ALTER TABLE ONLY public."PROFESIONAL" DROP CONSTRAINT "PROFESIONAL_pkey";
       public                 postgres    false    218            5           2606    25102    SERVICIO SERVICIO_pkey 
   CONSTRAINT     a   ALTER TABLE ONLY public."SERVICIO"
    ADD CONSTRAINT "SERVICIO_pkey" PRIMARY KEY (id_servicio);
 D   ALTER TABLE ONLY public."SERVICIO" DROP CONSTRAINT "SERVICIO_pkey";
       public                 postgres    false    219            1           2606    25087    USUARIO USUARIO_pkey 
   CONSTRAINT     _   ALTER TABLE ONLY public."USUARIO"
    ADD CONSTRAINT "USUARIO_pkey" PRIMARY KEY (rut_usuario);
 B   ALTER TABLE ONLY public."USUARIO" DROP CONSTRAINT "USUARIO_pkey";
       public                 postgres    false    217            9           2606    25113    CONTRATO id_profesional    FK CONSTRAINT     �   ALTER TABLE ONLY public."CONTRATO"
    ADD CONSTRAINT id_profesional FOREIGN KEY (id_profesional) REFERENCES public."PROFESIONAL"(id_profesional) NOT VALID;
 C   ALTER TABLE ONLY public."CONTRATO" DROP CONSTRAINT id_profesional;
       public               postgres    false    218    220    4659            <           2606    25126    RESEÑA id_profesional    FK CONSTRAINT     �   ALTER TABLE ONLY public."RESEÑA"
    ADD CONSTRAINT id_profesional FOREIGN KEY (id_profesional) REFERENCES public."PROFESIONAL"(id_profesional);
 B   ALTER TABLE ONLY public."RESEÑA" DROP CONSTRAINT id_profesional;
       public               postgres    false    4659    221    218            :           2606    25118    CONTRATO id_servicio    FK CONSTRAINT     �   ALTER TABLE ONLY public."CONTRATO"
    ADD CONSTRAINT id_servicio FOREIGN KEY (id_servicio) REFERENCES public."SERVICIO"(id_servicio) NOT VALID;
 @   ALTER TABLE ONLY public."CONTRATO" DROP CONSTRAINT id_servicio;
       public               postgres    false    220    4661    219            8           2606    25093    PROFESIONAL rut_usuario    FK CONSTRAINT     �   ALTER TABLE ONLY public."PROFESIONAL"
    ADD CONSTRAINT rut_usuario FOREIGN KEY (rut_usuario) REFERENCES public."USUARIO"(rut_usuario);
 C   ALTER TABLE ONLY public."PROFESIONAL" DROP CONSTRAINT rut_usuario;
       public               postgres    false    217    218    4657            ;           2606    25108    CONTRATO rut_usuario    FK CONSTRAINT     �   ALTER TABLE ONLY public."CONTRATO"
    ADD CONSTRAINT rut_usuario FOREIGN KEY (rut_usuario) REFERENCES public."USUARIO"(rut_usuario) NOT VALID;
 @   ALTER TABLE ONLY public."CONTRATO" DROP CONSTRAINT rut_usuario;
       public               postgres    false    4657    220    217            =           2606    25131    RESEÑA rut_usuario    FK CONSTRAINT     �   ALTER TABLE ONLY public."RESEÑA"
    ADD CONSTRAINT rut_usuario FOREIGN KEY (rut_usuario) REFERENCES public."USUARIO"(rut_usuario);
 ?   ALTER TABLE ONLY public."RESEÑA" DROP CONSTRAINT rut_usuario;
       public               postgres    false    221    217    4657            �      x������ � �      �      x������ � �      �      x������ � �      �      x������ � �      �      x������ � �     