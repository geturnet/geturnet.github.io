<?php
/**
 * Geturnet Theme Functions and Definitions
 */

if ( ! defined( '_S_VERSION' ) ) {
    define( '_S_VERSION', '1.0.0' );
}

function geturnet_setup() {
    // Mengaktifkan dukungan Title Tag otomatis
    add_theme_support( 'title-tag' );

    // Mengaktifkan Featured Image (Gambar Utama Postingan)
    add_theme_support( 'post-thumbnails' );

    // Mendaftarkan Lokasi Menu Navigasi Utama
    register_nav_menus( array(
        'menu-utama' => esc_html__( 'Menu Utama Geturnet', 'geturnet' ),
        'menu-footer' => esc_html__( 'Menu Footer Geturnet', 'geturnet' ),
    ) );
}
add_action( 'after_setup_theme', 'geturnet_setup' );

/**
 * Enqueue Styles and Scripts
 */
function geturnet_scripts() {
    wp_enqueue_style( 'geturnet-style', get_stylesheet_uri(), array(), _S_VERSION );
    wp_enqueue_style( 'font-awesome', 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css', array(), '6.4.0' );
    wp_enqueue_style( 'google-fonts', 'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap', array(), _S_VERSION );
}
add_action( 'wp_enqueue_scripts', 'geturnet_scripts' );
