<?php
/**
 * The header for Geturnet WordPress Theme
 */
?>
<!DOCTYPE html>
<html <?php language_attributes(); ?>>
<head>
    <meta charset="<?php bloginfo( 'charset' ); ?>">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="profile" href="https://gmpg.org/xfn/11">
    
    <!-- Google AdSense Account Verification & Auto Ads -->
    <meta name="google-adsense-account" content="ca-pub-4549220738609468">
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-4549220738609468" crossorigin="anonymous"></script>

    <?php wp_head(); ?>
</head>

<body <?php body_class(); ?>>
<?php wp_body_open(); ?>

    <!-- Overlay untuk efek gelap saat slide menu mobile terbuka -->
    <div class="overlay" id="overlay"></div>

    <!-- Top Bar -->
    <div class="top-bar">
        <div class="container top-bar-flex">
            <div><?php echo date_i18n('l, j F Y'); ?> | Geturnet Indonesia Newsroom</div>
            <div class="social-icons">
                <a href="#"><i class="fab fa-facebook-f"></i></a>
                <a href="#"><i class="fab fa-twitter"></i></a>
                <a href="#"><i class="fab fa-instagram"></i></a>
                <a href="#"><i class="fab fa-youtube"></i></a>
            </div>
        </div>
    </div>

    <!-- Main Header -->
    <header>
        <div class="container main-header">
            <div class="header-left">
                <!-- Tombol Hamburger untuk Mobile -->
                <button class="menu-toggle" id="menuToggle"><i class="fas fa-bars"></i></button>
                <a href="<?php echo esc_url( home_url( '/' ) ); ?>" class="logo">GETUR<span>NET</span></a>
            </div>
            
            <!-- Search Box -->
            <div class="search-box">
                <form role="search" method="get" action="<?php echo esc_url( home_url( '/' ) ); ?>">
                    <input type="text" name="s" placeholder="Cari berita, riset AI..." value="<?php echo get_search_query(); ?>">
                    <button type="submit"><i class="fas fa-search"></i></button>
                </form>
            </div>
        </div>

        <!-- Navigation Bar -->
        <nav>
            <div class="container nav-container">
                <ul class="nav-links" id="navLinks">
                    <!-- Tombol Close untuk Sidebar Mobile -->
                    <button class="sidebar-close" id="sidebarClose"><i class="fas fa-times"></i></button>
                    
                    <li><a href="<?php echo esc_url( home_url( '/category/terkini/' ) ); ?>">Terkini</a></li>
                    <li><a href="<?php echo esc_url( home_url( '/category/terpopuler/' ) ); ?>">Terpopuler</a></li>
                    <li><a href="<?php echo esc_url( home_url( '/category/bisnis/' ) ); ?>">Bisnis</a></li>
                    <li><a href="<?php echo esc_url( home_url( '/category/green/' ) ); ?>">Green</a></li>
                    <li><a href="<?php echo esc_url( home_url( '/category/tech/' ) ); ?>">Tech</a></li>
                    <li><a href="<?php echo esc_url( home_url( '/category/bola/' ) ); ?>">Bola</a></li>
                    <li><a href="<?php echo esc_url( home_url( '/category/sport/' ) ); ?>">Sport</a></li>
                    <li><a href="<?php echo esc_url( home_url( '/category/lifestyle/' ) ); ?>">Lifestyle</a></li>
                    <li><a href="<?php echo esc_url( home_url( '/category/entertainment/' ) ); ?>">Entertainment</a></li>
                    <li><a href="<?php echo esc_url( home_url( '/category/otomotif/' ) ); ?>">Otomotif</a></li>
                    <li><a href="<?php echo esc_url( home_url( '/category/tekno/' ) ); ?>">Tekno</a></li>
                    <li><a href="<?php echo esc_url( home_url( '/category/health/' ) ); ?>">Health</a></li>
                    <li><a href="<?php echo esc_url( home_url( '/category/foto/' ) ); ?>">Foto</a></li>
                    <li><a href="<?php echo esc_url( home_url( '/category/video/' ) ); ?>">Video</a></li>
                    <li><a href="<?php echo esc_url( home_url( '/category/opini/' ) ); ?>">Opini</a></li>

                    <!-- Dropdown Menu: Regional -->
                    <li class="dropdown-container">
                        <a href="#" class="dropdown-toggle">Regional <i class="fas fa-chevron-down" style="font-size: 10px;"></i></a>
                        <ul class="dropdown-menu">
                            <li><a href="<?php echo esc_url( home_url( '/category/jakarta/' ) ); ?>">Jakarta</a></li>
                            <li><a href="<?php echo esc_url( home_url( '/category/jabar/' ) ); ?>">Jabar</a></li>
                            <li><a href="<?php echo esc_url( home_url( '/category/jatim/' ) ); ?>">Jatim</a></li>
                            <li><a href="<?php echo esc_url( home_url( '/category/jateng/' ) ); ?>">Jateng</a></li>
                            <li><a href="<?php echo esc_url( home_url( '/category/sumut/' ) ); ?>">Sumut</a></li>
                            <li><a href="<?php echo esc_url( home_url( '/category/banten/' ) ); ?>">Banten</a></li>
                            <li><a href="<?php echo esc_url( home_url( '/category/sulsel/' ) ); ?>">Sulsel</a></li>
                            <li><a href="<?php echo esc_url( home_url( '/category/bali/' ) ); ?>">Bali</a></li>
                            <li><a href="<?php echo esc_url( home_url( '/category/sumsel/' ) ); ?>">Sumsel</a></li>
                            <li><a href="<?php echo esc_url( home_url( '/category/jogja/' ) ); ?>">Jogja</a></li>
                            <li><a href="<?php echo esc_url( home_url( '/category/riau/' ) ); ?>">Riau</a></li>
                            <li><a href="<?php echo esc_url( home_url( '/category/lampung/' ) ); ?>">Lampung</a></li>
                            <li><a href="<?php echo esc_url( home_url( '/category/kaltim/' ) ); ?>">Kaltim</a></li>
                            <li><a href="<?php echo esc_url( home_url( '/category/kalbar/' ) ); ?>">Kalbar</a></li>
                            <li><a href="<?php echo esc_url( home_url( '/category/sumbar/' ) ); ?>">Sumbar</a></li>
                            <li><a href="<?php echo esc_url( home_url( '/category/bogor/' ) ); ?>">Bogor</a></li>
                            <li><a href="<?php echo esc_url( home_url( '/category/bekasi/' ) ); ?>">Bekasi</a></li>
                            <li><a href="<?php echo esc_url( home_url( '/category/malang/' ) ); ?>">Malang</a></li>
                            <li><a href="<?php echo esc_url( home_url( '/category/surakarta/' ) ); ?>">Surakarta</a></li>
                            <li><a href="<?php echo esc_url( home_url( '/category/batam/' ) ); ?>">Batam</a></li>
                        </ul>
                    </li>

                    <!-- Dropdown Menu: Riset & AI -->
                    <li class="dropdown-container">
                        <a href="#" class="dropdown-toggle">Riset & AI <i class="fas fa-chevron-down" style="font-size: 10px;"></i></a>
                        <ul class="dropdown-menu">
                            <li><a href="#">Data Riset & Pengembangan AI</a></li>
                            <li><a href="#">Media Monitoring</a></li>
                            <li><a href="#">Generative Engine Optimization</a></li>
                        </ul>
                    </li>
                </ul>
            </div>
        </nav>
    </header>

    <!-- Contoh Unit Iklan AdSense di bawah Header (Opsional) -->
    <div class="container" style="margin: 20px auto; text-align: center;">
        <ins class="adsbygoogle"
             style="display:block"
             data-ad-client="ca-pub-4549220738609468"
             data-ad-slot="xxxxx"
             data-ad-format="auto"
             data-full-width-responsive="true"></ins>
        <script>
             (adsbygoogle = window.adsbygoogle || []).push({});
        </script>
    </div>

    <!-- JavaScript untuk Interaksi Mobile & Dropdown -->
    <script>
        document.addEventListener("DOMContentLoaded", function() {
            const menuToggle = document.getElementById('menuToggle');
            const sidebarClose = document.getElementById('sidebarClose');
            const navLinks = document.getElementById('navLinks');
            const overlay = document.getElementById('overlay');

            if(menuToggle) {
                menuToggle.addEventListener('click', () => {
                    navLinks.classList.add('active');
                    overlay.classList.add('active');
                });
            }

            function closeMenu() {
                navLinks.classList.remove('active');
                overlay.classList.remove('active');
            }

            if(sidebarClose) sidebarClose.addEventListener('click', closeMenu);
            if(overlay) overlay.addEventListener('click', closeMenu);

            const dropdownToggles = document.querySelectorAll('.dropdown-toggle');
            dropdownToggles.forEach(toggle => {
                toggle.addEventListener('click', function(e) {
                    e.preventDefault();
                    const dropdownMenu = this.nextElementSibling;
                    if(dropdownMenu) dropdownMenu.classList.toggle('show');
                });
            });
        });
    </script>
