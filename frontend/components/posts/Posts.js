import Image from "next/image";
import React from "react";
import Link from 'next/link';

export default function Posts({post}) {
    return (
        <div>
            <Link href={`/post/${post.slug}`}>
                <div class="max-w-sm rounded overflow-hidden shadow-lg">
                    <img class="w-full h-60" src="/lion.jpg" alt="Sunset in the mountains" />
                    <div class="px-2 py-2">
                        <div class="font-semibold text-lg mb-2">{post.title}</div>
                        <p class="text-gray-700 text-base">
                            {post.content}
                        </p>
                    </div>
                    <div class="px-6 pt-4 pb-2">
                        <span class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">
                            {post.category.title}
                        </span>
                    </div>
                </div>
            </Link>
        </div>
    )
}