<?php
/**
 * The template for displaying all single pages (Static Pages)
 *
 * @package Geturnet
 */

get_header();
?>

<div class="container main-container" style="display: grid; grid-template-columns: 2.2fr 1fr; gap: 30px; margin: 30px auto; max-width: 1200px; padding: 0 15px;">
    
    <!-- Konten Utama Halaman Statis -->
    <main>
        <?php
        while ( have_posts() ) :
            the_post();
        ?>
            <article id="post-<?php the_ID(); ?>" <?php post_class(); ?>>
                
                <!-- Judul Halaman -->
                <h1 style="font-size: 32px; font-weight: 800; line-height: 1.3; margin-bottom: 20px; color: #222; border-bottom: 2px solid #d32f2f; padding-bottom: 10px;">
                    <?php the_title(); ?>
                </h1>

                <!-- Featured Image (Opsional jika di-upload) -->
                <?php if ( has_post_thumbnail() ) : ?>
                    <div class="featured-image" style="margin-bottom: 25px;">
                        <?php the_post_thumbnail('large', array('style' => 'width:100%; height:auto; max-height:400px; object-fit:cover; border-radius:6px;')); ?>
                    </div>
                <?php endif; ?>

                <!-- Isi Konten Halaman (Dibuat melalui Dashboard WordPress) -->
                <div class="page-content" style="font-size: 16px; line-height: 1.8; color: #333; margin-bottom: 40px;">
                    <?php 
                    the_content(); 

                    // Menangani pagination jika halaman statis cukup panjang
                    wp_link_pages( array(
                        'before' => '<div class="page-links" style="margin-top: 20px; font-weight: 600;">' . esc_html__( 'Halaman:', 'geturnet' ),
                        'after'  => '</div>',
                    ) );
                    ?>
                </div>

                <!-- Bagian Kotak Informasi Tambahan / Hubungi Kami -->
                <div class="info-box" style="background: #f9f9f9; border-left: 4px solid #d32f2f; padding: 20px; border-radius: 4px; margin-top: 30px;">
                    <h3 style="font-size: 16px; font-weight: 700; margin-bottom: 8px; color: #111;">Butuh Informasi Lebih Lanjut?</h3>
                    <p style="font-size: 14px; color: #666; margin: 0;">
                        Hubungi tim redaksi atau manajemen Geturnet melalui halaman <a href="<?php echo esc_url( home_url( '/kontak/' ) ); ?>" style="color: #d32f2f; font-weight: 600; text-decoration: underline;">Kontak Kami</a> atau kirimkan email langsung ke redaksi.
                    </p>
                </div>

            </article>
        <?php endwhile; ?>
    </main>

    <!-- Sidebar / Terpopuler -->
    <aside>
        <div class="sidebar-box" style="background: #f9f9f9; border: 1px solid #e0e0e0; padding: 20px; border-radius: 6px;">
            <div class="section-title" style="font-size: 18px; font-weight: 700; border-left: 4px solid #d32f2f; padding-left: 10px; margin-bottom: 20px; text-transform: uppercase;">
                Terpopuler
            </div>
            <?php
            $popular_posts = new WP_Query( array(
                'posts_per_page' => 4,
                'orderby' => 'comment_count',
                'order' => 'DESC'
            ) );

            $num = 1;
            if ( $popular_posts->have_posts() ) :
                while ( $popular_posts->have_posts() ) : $popular_posts->the_post();
            ?>
                <div class="trending-item" style="display: flex; gap: 15px; margin-bottom: 15px; padding-bottom: 15px; border-bottom: 1px solid #e0e0e0; align-items: flex-start;">
                    <div class="trending-num" style="font-size: 24px; font-weight: 800; color: #ccc; min-width: 25px;"><?php echo $num++; ?></div>
                    <div>
                        <h4 style="font-size: 14px; font-weight: 600; line-height: 1.3;">
                            <a href="<?php the_permalink(); ?>" style="text-decoration:none; color:#222;"><?php the_title(); ?></a>
                        </h4>
                        <div class="meta-info" style="font-size: 12px; color: #666; margin-top: 5px;"><?php echo get_the_date(); ?></div>
                    </div>
                </div>
            <?php
                endwhile;
                wp_reset_postdata();
            endif;
            ?>
        </div>
    </aside>

</div>

<?php
get_footer();
