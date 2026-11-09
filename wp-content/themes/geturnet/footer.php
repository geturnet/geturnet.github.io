<?php
/**
 * The template for displaying the footer
 */
?>
    <!-- Footer -->
    <footer>
        <div class="container footer-grid">
            <div class="footer-col">
                <h3 class="logo" style="color:#fff;">GETUR<span>NET</span></h3>
                <p style="font-size:13px; color:#aaa; margin-top:10px;">
                    Portal berita nasional, riset AI, regional, dan teknologi terdepan menyajikan informasi aktual dan terpercaya.
                </p>
            </div>
            
            <div class="footer-col">
                <h3>Redaksi &amp; Informasi</h3>
                <ul>
                    <li><a href="<?php echo esc_url( home_url( '/redaksi/' ) ); ?>">Redaksi</a></li>
                    <li><a href="<?php echo esc_url( home_url( '/kontak/' ) ); ?>">Kontak</a></li>
                    <li><a href="<?php echo esc_url( home_url( '/tentang-kami/' ) ); ?>">Tentang Kami</a></li>
                    <li><a href="<?php echo esc_url( home_url( '/karir/' ) ); ?>">Karir</a></li>
                </ul>
            </div>

            <div class="footer-col">
                <h3>Kebijakan &amp; Bantuan</h3>
                <ul>
                    <li><a href="<?php echo esc_url( home_url( '/pedoman-media-siber/' ) ); ?>">Pedoman Media Siber</a></li>
                    <li><a href="<?php echo esc_url( home_url( '/kebijakan-privasi/' ) ); ?>">Kebijakan Privasi</a></li>
                    <li><a href="<?php echo esc_url( home_url( '/saran-dan-kritik/' ) ); ?>">Saran dan Kritik</a></li>
                    <li><a href="<?php echo esc_url( home_url( '/site-map/' ) ); ?>">Site Map</a></li>
                </ul>
            </div>
        </div>
        
        <div class="copyright">
            &copy; 2026 Geturnet Ltd. All Rights Reserved.
        </div>
    </footer>

    <?php wp_footer(); ?>
</body>
</html>
