FROM php:8.4-fpm

RUN apt-get update && apt-get install -y \
    git \
    curl \
    libpng-dev \
    libonig-dev \
    libxml2-dev \
    zip \
    unzip \
    libpq-dev


RUN docker-php-ext-install pdo pdo_pgsql mbstring exif pcntl bcmath


COPY --from=composer:latest /usr/bin/composer /usr/bin/composer

WORKDIR /var/www/html


EXPOSE 8000

CMD ["php", "-S", "0.0.0.0:8000", "-t", "/var/www/html/public"]