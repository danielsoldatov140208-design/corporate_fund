import React from 'react';
import { createRoot } from 'react-dom/client';

function DjangoNotice() {
    return (
        <main className="django-notice">
            <span className="django-notice__eyebrow">REGION FORWARD · DJANGO</span>
            <h1>Этот сайт работает на Django</h1>
            <p>
                Основные страницы и переводы находятся в Django-шаблонах.
                Запустите сервер командой <code>python manage.py runserver</code>.
            </p>
            <a href="http://127.0.0.1:8000/">Открыть сайт</a>
        </main>
    );
}

createRoot(document.getElementById('root')).render(<DjangoNotice />);
