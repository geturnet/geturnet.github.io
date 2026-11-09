<?php
/**
 * The template for displaying all single posts
 */
get_header();
?>

<div class="container main-container" style="display: grid; grid-template-columns: 2.2fr 1fr; gap: 30px; margin: 30px auto; max-width: 1200px; padding: 0 15px;">
    
    <!-- Konten Utama Artikel -->
    <main>
        <?php
        while ( have_posts() ) :
            the_post();
        ?>
            <article id="post-<?php the_ID(); ?>" <?php post_class(); ?>>
                <div class="category-tag" style="display:inline-block; background:#d32f2f; color:white; font-size:11px; font-weight:700; padding:3px 8px; border-radius:3px; margin-bottom: 12px; text-transform: uppercase;">
                    <?php 
                    $categories = get_the_category();
                    if ( ! empty( $categories ) ) {
                        echo esc_html( $categories[0]->name );
                    }
                    ?>
                </div>

                <h1 style="font-size: 28px; font-weight: 700; line-height: 1.3; margin-bottom: 15px;"><?php the_title(); ?></h1>
                
                <div class="meta-info" style="font-size: 13px; color: #666; margin-bottom: 20px; border-bottom: 1px solid #e0e0e0; padding-bottom: 10px;">
                    <i class="far fa-clock"></i> <?php echo get_the_date(); ?> • Oleh <strong><?php the_author(); ?></strong>
                </div>

                <?php if ( has_post_thumbnail() ) : ?>
                    <div class="featured-image" style="margin-bottom: 25px;">
                        <?php the_post_thumbnail('large', array('style' => 'width:100%; height:auto; max-height:450px; object-fit:cover; border-radius:6px;')); ?>
                    </div>
                <?php endif; ?>

                <!-- Isi Artikel Berita -->
                <div class="article-content" style="font-size: 16px; line-height: 1.8; color: #333;">
                    <?php the_content(); ?>
                </div>

                <!-- Bagian Iklan AdSense di Bawah Artikel -->
                <div class="adsense-bottom" style="margin: 30px 0; text-align: center;">
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
