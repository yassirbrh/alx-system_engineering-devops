# Puppet manifest to install Nginx Server.

exec { 'install_nginx':
    provider => shell,
    command  => 'apt-get -y update && apt-get install -y nginx; mkdir -p /var/www/helloworld;
    echo "Hello World!" > /var/www/helloworld/index.html; echo "http {
        root /var/www/helloworld;
        index index.html;
        server {
                listen 80;
                location \ {
                }
                location /redirect_me {
                    return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
                }
                error_page 404 /404_redirection;
                location = /404_redirection {
                        internal;
                        return 404 \"Ceci n\'est pas une page\n\n\";
                }
        }
    }
    events {
    }" > /etc/nginx/nginx.conf; service nginx start;'
}