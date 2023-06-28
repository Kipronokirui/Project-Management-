import React from 'react';
import Head from 'next/head';
import { useRouter } from 'next/router';

export default function PostDetail({ data }) {
    const { query: { slug } } = useRouter()
    return (
      <>
        <Head>
            <title>Post Details</title>
            <meta name="description" content={data.title} />
            <link rel="icon" href="/logo.ico" />
        </Head>
        <main class="pt-8 pb-16 lg:pt-16 lg:pb-24 bg-white dark:bg-gray-900">
            <div class="flex justify-between px-4 mx-auto max-w-screen-xl ">
                <article class="mx-auto w-full max-w-2xl format format-sm sm:format-base lg:format-lg format-blue dark:format-invert">
                    <header class="mb-4 lg:mb-6 not-format">
                        <address class="flex items-center mb-6 not-italic">
                            <div class="inline-flex items-center mr-3 text-sm text-gray-900 dark:text-white">
                                <img class="mr-4 w-16 h-16 rounded-full" src="https://flowbite.com/docs/images/people/profile-picture-2.jpg" alt="Jese Leos" />
                                <div>
                                        <a href="#" rel="author" class="text-xl font-bold text-gray-900 dark:text-white">{data.author.email}</a>
                                    <p class="text-base font-light text-gray-500 dark:text-gray-400">Graphic Designer, educator & CEO Flowbite</p>
                                    <p class="text-base font-light text-gray-500 dark:text-gray-400"><time pubdate datetime="2022-02-08" title="February 8th, 2022">Feb. 8, 2022</time></p>
                                </div>
                            </div>
                        </address>
                        <h1 class="mb-4 text-3xl font-extrabold leading-tight text-gray-900 lg:mb-6 lg:text-4xl dark:text-white">
                            {data.title}
                        </h1>
                    </header>
                    <div>
                        {data.content}
                    </div>    
                </article>
            </div>
        </main>
      </>
    
  )
}
export async function getStaticPaths() {
    const response = await fetch('http://127.0.0.1:8000/posts/')
    const data = await response.json();
    const allSlugs = data.map(item => item.slug)
    const paths = allSlugs.map(slug => ({ params: { slug: slug } }))
    
    return {
      paths,
      fallback:false,
    }
  }
export async function getStaticProps({params}) {
    const response = await fetch(`http://127.0.0.1:8000/post/${params.slug}`);
    const data = await response.json();
  
    return {
      props: {
        data,
      },
    }
  }