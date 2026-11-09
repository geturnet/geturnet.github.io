<?php
/**
 * The main template file (Geturnet Portal Berita)
 */
get_header();
?>

<div class="container main-container" style="display: grid; grid-template-columns: 2.2fr 1fr; gap: 30px; margin: 30px auto; max-width: 1200px; padding: 0 15px;">
    
    <!-- Kolom Konten Utama / Berita -->
    <main>
        <?php if ( have_posts() ) : ?>
            <div class="section-title" style="font-size: 18px; font-weight: 700; border-left: 4px solid #d32f2f; padding-left: 10px; margin-bottom: 20px; text-transform: uppercase;">
                Berita Terkini &amp; Pilihan
            </div>

            <div class="news-grid" style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px;">
                <?php while ( have_posts() ) : the_post(); ?>
                    <div class="news-card">
                        <?php if ( has_post_thumbnail() ) : ?>
                            <a href="<?php the_permalink(); ?>">
                                <?php the_post_thumbnail('medium', array('style' => 'width:100%; height:150px; object-fit:cover; border-radius:4px;')); ?>
                            </a>
                        <?php endif; ?>
                        
                        <div class="category-tag" style="display:inline-block; background:#d32f2f; color:white; font-size:11px; font-weight:700; padding:3px 8px; border-radius:3px; margin:12px 0 8px 0; text-transform:uppercase;">
                            <?php 
                            $categories = get_the_category();
                            if ( ! empty( $categories ) ) {
                                echo esc_html( $categories[0]->name );
                            }
                            ?>
                        </div>

                        <h3 style="font-size: 15px; font-weight: 600; margin: 8px 0; line-height: 1.4;">
                            <a href="<?php the_permalink(); ?>" style="text-decoration:none; color:#222;"><?php the_title(); ?></a>
                        </h3>
                        
                        <div class="meta-info" style="font-size: 13px; color: #666;">
                            <i class="far fa-clock"></i> <?php echo get_the_date(); ?>
                        </div>
                    </div>
                <?php endwhile; ?>
            </div>

        <?php else : ?>
            <p>Belum ada berita yang dipublikasikan.</p>
        <?php endif; ?>
    </main>

    <!-- Sidebar / Terpopuler -->
    <aside>
        <div class="sidebar-box" style="background: #f9f9f9; border: 1px solid #e0e0e0; padding: 20px; border-radius: 6px;">
            <div class="section-title" style="font-size: 18px; font-weight: 700; border-left: 4px solid #d32f2f; padding-left: 10px; margin-bottom: 20px; text-transform: uppercase;">
                Terpopuler
            </div>
            <?php
            // Query untuk mengambil postingan populer (berdasarkan komentar atau views)
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
