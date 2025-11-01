function toggleSidebar() {
    const sidebar = document.getElementById('sidebar');
    const mainContent = document.getElementById('mainContent');
    const toggleIcon = document.getElementById('toggleIcon');
    
    sidebar.classList.toggle('collapsed');
    mainContent.classList.toggle('expanded');
    
    if (sidebar.classList.contains('collapsed')) {
        toggleIcon.className = 'fas fa-chevron-right';
    } else {
        toggleIcon.className = 'fas fa-chevron-left';
    }
}

function toggleSubmenu(event) {
    event.preventDefault();
    const submenu = event.target.closest('li').querySelector('.submenu');
    const arrow = event.target.closest('a').querySelector('.submenu-arrow');
    
    submenu.classList.toggle('show');
    arrow.classList.toggle('rotated');
}

        // Mobile sidebar toggle
        function toggleMobileSidebar() {
            const sidebar = document.getElementById('sidebar');
            sidebar.classList.toggle('show');
        }

        // Active menu item handling
        document.querySelectorAll('.nav-menu a').forEach(link => {
            link.addEventListener('click', function(e) {
                // Ne pas empêcher la navigation pour les liens avec href
                if (this.getAttribute('href') !== '#') {
                    return; // Laisser le navigateur suivre le lien
                }
                
                e.preventDefault(); // Empêcher seulement pour les liens #
                
                // Remove active class from all links
                document.querySelectorAll('.nav-menu a').forEach(l => l.classList.remove('active'));
                
                // Add active class to clicked link
                this.classList.add('active');
            });
        });

        // Close sidebar on mobile when clicking outside
        document.addEventListener('click', function(e) {
            const sidebar = document.getElementById('sidebar');
            const mobileToggle = document.querySelector('.mobile-toggle');
            
            if (window.innerWidth <= 768 && 
                !sidebar.contains(e.target) && 
                !mobileToggle.contains(e.target)) {
                sidebar.classList.remove('show');
            }
        });

        // Handle window resize
        window.addEventListener('resize', function() {
            const sidebar = document.getElementById('sidebar');
            if (window.innerWidth > 768) {
                sidebar.classList.remove('show');
            }
        });

        function toggleSubmenu(event) {
            event.preventDefault();
            const submenu = event.currentTarget.nextElementSibling;
            submenu.classList.toggle('active');
        }

// =========================
//  Active Link Management
// =========================
document.querySelectorAll('.nav-menu a').forEach(link => {
    link.addEventListener('click', function (e) {
        // Laisser passer tous les liens qui ne sont pas juste "#"
        if (this.getAttribute('href') && this.getAttribute('href') !== '#') {
            return;
        }
        e.preventDefault();

        document.querySelectorAll('.nav-menu a').forEach(l => l.classList.remove('active'));
        this.classList.add('active');
    });
});

// =========================
//  Close Sidebar on Mobile
// =========================
document.addEventListener('click', function (e) {
    const sidebar = document.getElementById('sidebar');
    const mobileToggle = document.querySelector('.mobile-toggle');

    if (window.innerWidth <= 768 &&
        !sidebar.contains(e.target) &&
        !mobileToggle?.contains(e.target)) {
        sidebar.classList.remove('show');
    }
});